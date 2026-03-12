#!/usr/bin/env python3
"""
Topic Parser Script
Parses enhanced markdown files and generates Copilot Studio setup checklists.

Usage:
    python scripts/parse_topics.py                    # Parse all topic files
    python scripts/parse_topics.py --topic Morning_Brief  # Parse specific topic
    python scripts/parse_topics.py --output json      # Output as JSON
"""

import os
import re
import json
import argparse
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional
from datetime import datetime


@dataclass
class Topic:
    """Represents a Copilot Studio Topic"""
    name: str
    description: str = ""
    priority: int = 0
    triggers: List[str] = field(default_factory=list)
    action_type: str = ""  # agent, flow, etc.
    action_target: str = ""
    connectors: List[str] = field(default_factory=list)
    steps: List[Dict] = field(default_factory=list)
    setup_checklist: List[str] = field(default_factory=list)


@dataclass
class FlowStep:
    """Represents a flow step"""
    number: int
    name: str
    description: str
    action: str
    connector: str
    parameters: str
    output: str
    condition: str = ""


class TopicParser:
    """Parser for enhanced markdown files with Copilot Studio annotations"""
    
    ANNOTATION_PATTERNS = {
        'topic': r'<!--\s*@topic:(\w+)\s*-->',
        'topic_description': r'<!--\s*@topic:description:([^)]*?)\s*-->',
        'topic_priority': r'<!--\s*@topic:priority:(\d+)\s*-->',
        'trigger': r'<!--\s*@trigger:([^)]*?)\s*-->',
        'action_agent': r'<!--\s*@action:agent:([^)]*?)\s*-->',
        'action_connector': r'<!--\s*@action:connector:([^)]*?)\s*-->',
        'step': r'<!--\s*@step:(\d+)\s*-->',
        'step_name': r'<!--\s*@step:name:([^)]*?)\s*-->',
        'step_description': r'<!--\s*@step:description:([^)]*?)\s*-->',
        'step_action': r'<!--\s*@step:action:([^)]*?)\s*-->',
        'step_connector': r'<!--\s*@step:connector:([^)]*?)\s*-->',
        'step_parameters': r'<!--\s*@step:parameters:([^)]*?)\s*-->',
        'step_output': r'<!--\s*@step:output:([^)]*?)\s*-->',
        'step_condition': r'<!--\s*@step:condition:([^)]*?)\s*-->',
        'connector': r'<!--\s*@connectors?\s*-->\s*\n(.*?)(?=\n<!--|\n\n|\Z)',
        'setup_checklist': r'<!--\s*@setup_checklist\s*-->\s*\n(.*?)(?=<!--|\n##|\Z)',
    }
    
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.topics: List[Topic] = []
    
    def parse_file(self, file_path: str, topic_name: str = None) -> Optional[Topic]:
        """Parse a single markdown file and extract topic information"""
        path = self.base_path / file_path
        if not path.exists():
            print(f"Warning: File not found: {path}")
            return None
        
        content = path.read_text(encoding='utf-8')
        
        # Extract basic topic info
        topic = Topic(
            name=self._extract_pattern(content, self.ANNOTATION_PATTERNS['topic']),
            description=self._extract_pattern(content, self.ANNOTATION_PATTERNS['topic_description']),
            priority=int(self._extract_pattern(content, self.ANNOTATION_PATTERNS['topic_priority']) or 0)
        )
        
        # If topic_name specified, verify it matches
        if topic_name and topic.name != topic_name:
            return None
        
        # Extract triggers - match only the content between @trigger: and -->
        trigger_lines = re.findall(r'@trigger:([^#\s-][^->]*)', content)
        topic.triggers = [t.strip() for t in trigger_lines if t.strip()]
        
        # Extract action
        topic.action_target = self._extract_pattern(content, self.ANNOTATION_PATTERNS['action_agent'])
        topic.action_type = "agent" if topic.action_target else "flow"
        
        # Extract connectors
        connectors_match = re.search(self.ANNOTATION_PATTERNS['connector'], content, re.DOTALL)
        if connectors_match:
            connector_text = connectors_match.group(1)
            topic.connectors = [c.strip() for c in connector_text.split(',')]
        
        # Extract flow steps
        topic.steps = self._extract_steps(content)
        
        # Extract setup checklist
        checklist_match = re.search(self.ANNOTATION_PATTERNS['setup_checklist'], content, re.DOTALL)
        if checklist_match:
            checklist_text = checklist_match.group(1)
            topic.setup_checklist = [
                line.strip().lstrip('- [ ] ').lstrip('- [x] ')
                for line in checklist_text.split('\n')
                if line.strip().startswith('- [')
            ]
        
        return topic
    
    def _extract_pattern(self, content: str, pattern: str) -> str:
        """Extract a single pattern match"""
        match = re.search(pattern, content)
        return match.group(1).strip() if match else ""
    
    def _extract_steps(self, content: str) -> List[Dict]:
        """Extract flow steps from content"""
        steps = []
        
        # Find all step blocks
        step_pattern = r'<!--\s*@step:(\d+)\s*-->.*?###\s+Step\s+\d+:[^#]*?(?=<!--\s*@step:|<!--\s*@flow:end|##|\Z)'
        step_blocks = re.findall(step_pattern, content, re.DOTALL)
        
        for block in step_blocks:
            step_match = re.search(r'<!--\s*@step:(\d+)\s*-->.*?###\s+Step\s+\d+:\s*([^\n]+)', block, re.DOTALL)
            if step_match:
                step_num = int(step_match.group(1))
                step_name = self._extract_pattern(block, self.ANNOTATION_PATTERNS['step_name'])
                step_desc = self._extract_pattern(block, self.ANNOTATION_PATTERNS['step_description'])
                step_action = self._extract_pattern(block, self.ANNOTATION_PATTERNS['step_action'])
                step_connector = self._extract_pattern(block, self.ANNOTATION_PATTERNS['step_connector'])
                step_params = self._extract_pattern(block, self.ANNOTATION_PATTERNS['step_parameters'])
                step_output = self._extract_pattern(block, self.ANNOTATION_PATTERNS['step_output'])
                
                steps.append({
                    'number': step_num,
                    'name': step_name,
                    'description': step_desc,
                    'action': step_action,
                    'connector': step_connector,
                    'parameters': step_params,
                    'output': step_output
                })
        
        return steps
    
    def parse_all(self, pattern: str = "**/*.md") -> List[Topic]:
        """Parse all markdown files in the topics and subagents directories"""
        topics = []
        
        # Parse sub-agent files (these have individual topic definitions)
        subagent_files = [
            "subagents/Morning_Brief_Agent - System Prompt Instructions.md",
            "subagents/Friday_Wrap_Up_Agent - System Prompt Instructions.md",
            "subagents/Task_Review_Agent - System Prompt Instructions.md",
            "subagents/Email_Triage_Agent - System Prompt Instructions.md",
            "subagents/Progress_Summary_Agent - System Prompt Instructions.md",
            "subagents/Governance_Action_Agent - System Prompt Instructions.md",
        ]
        
        for file_path in subagent_files:
            topic = self.parse_file(file_path)
            if topic and topic.name:
                topics.append(topic)
        
        self.topics = topics
        return topics
    
    def generate_checklist(self, topic: Topic) -> str:
        """Generate a human-readable setup checklist for a topic"""
        lines = [
            f"# Setup Checklist: {topic.name}",
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            f"## Topic Configuration",
            f"- Name: {topic.name}",
            f"- Description: {topic.description}",
            f"- Priority: {topic.priority}",
            "",
            "## Trigger Phrases",
        ]
        
        for trigger in topic.triggers:
            lines.append(f'- [ ] Add trigger: "{trigger}"')
        
        lines.extend([
            "",
            "## Action",
            f"- Type: {topic.action_type}",
            f"- Target: {topic.action_target}",
            "",
            "## Connectors",
        ])
        
        for connector in topic.connectors:
            lines.append(f'- [ ] Configure: {connector}')
        
        if topic.steps:
            lines.extend([
                "",
                "## Flow Steps",
            ])
            for step in topic.steps:
                lines.extend([
                    f"### Step {step['number']}: {step['name']}",
                    f"- Action: {step['action']}",
                    f"- Connector: {step['connector']}",
                    f"- Parameters: {step['parameters'] or 'N/A'}",
                    f"- Output: {step['output'] or 'N/A'}",
                    "",
                ])
        
        if topic.setup_checklist:
            lines.extend([
                "",
                "## Setup Checklist",
            ])
            for item in topic.setup_checklist:
                lines.append(f"- [ ] {item}")
        
        return "\n".join(lines)
    
    def generate_json(self, topic: Optional[Topic] = None) -> str:
        """Generate JSON output"""
        if topic:
            return json.dumps(asdict(topic), indent=2)
        else:
            return json.dumps([asdict(t) for t in self.topics], indent=2)
    
    def generate_markdown_table(self) -> str:
        """Generate a markdown table of all topics"""
        lines = [
            "# Topic Summary",
            "",
            "| Topic | Priority | Triggers | Agent | Connectors |",
            "|-------|----------|----------|-------|------------|",
        ]
        
        for topic in sorted(self.topics, key=lambda t: t.priority):
            trigger_count = len(topic.triggers)
            connectors = ", ".join(topic.connectors) if topic.connectors else "N/A"
            lines.append(
                f"| {topic.name} | {topic.priority} | {trigger_count} | "
                f"{topic.action_target} | {connectors} |"
            )
        
        return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Parse enhanced markdown files for Copilot Studio Topics"
    )
    parser.add_argument(
        '--topic', '-t',
        help="Parse specific topic by name"
    )
    parser.add_argument(
        '--output', '-o',
        choices=['checklist', 'json', 'table'],
        default='checklist',
        help="Output format"
    )
    parser.add_argument(
        '--path', '-p',
        default='.',
        help="Base path for files"
    )
    
    args = parser.parse_args()
    
    parser_obj = TopicParser(args.path)
    topics = parser_obj.parse_all()
    
    if args.topic:
        topic = next((t for t in topics if t.name == args.topic), None)
        if not topic:
            print(f"Topic '{args.topic}' not found")
            return
        
        if args.output == 'json':
            print(parser_obj.generate_json(topic))
        else:
            print(parser_obj.generate_checklist(topic))
    else:
        if args.output == 'json':
            print(parser_obj.generate_json())
        elif args.output == 'table':
            print(parser_obj.generate_markdown_table())
        else:
            # Generate checklists for all topics
            for topic in sorted(topics, key=lambda t: t.priority):
                print(parser_obj.generate_checklist(topic))
                print("\n" + "=" * 80 + "\n")


if __name__ == "__main__":
    main()
# Enhanced Markdown Specification for Copilot Studio Topics

This specification defines a structured markdown format that makes it easy to translate documentation into Copilot Studio Topic flows.

---

## Annotation Schema

### Topic Metadata Annotations

| Annotation | Purpose | Example |
|------------|---------|---------|
| `<!-- @topic:name -->` | Defines a Copilot Studio Topic | `<!-- @topic:Morning_Brief -->` |
| `<!-- @topic:description -->` | Topic description | `<!-- @topic:description:Daily briefing workflow -->` |
| `<!-- @trigger -->` | Trigger phrase for the topic | `<!-- @trigger:morning brief -->` |
| `<!-- @action:agent -->` | Action to call an agent | `<!-- @action:agent:Morning_Brief_Agent -->` |
| `<!-- @action:connector -->` | Action to use a connector | `<!-- @action:connector:Microsoft Planner -->` |

### Flow Step Annotations

| Annotation | Purpose | Example |
|------------|---------|---------|
| `<!-- @step:N -->` | Defines a flow step number | `<!-- @step:1 -->` |
| `<!-- @step:name -->` | Step name | `<!-- @step:name:Get Tasks from Planner -->` |
| `<!-- @step:description -->` | Step description | `<!-- @step:description:List all tasks from Planner -->` |
| `<!-- @step:action -->` | Action to perform | `<!-- @step:action:List tasks -->` |
| `<!-- @step:connector -->` | Connector to use | `<!-- @step:connector:Microsoft Planner -->` |
| `<!-- @step:parameters -->` | Parameters for the action | `<!-- @step:parameters:PlanId={PlanId} -->` |
| `<!-- @step:condition -->` | Conditional logic | `<!-- @step:condition:If tasks > 0 -->` |
| `<!-- @step:output -->` | Output variable | `<!-- @step:output:TasksList -->` |

### Variable Annotations

| Annotation | Purpose | Example |
|------------|---------|---------|
| `<!-- @variable:name -->` | Define a variable | `<!-- @variable:name:OverdueTasks -->` |
| `<!-- @variable:type -->` | Variable type | `<!-- @variable:type:Array -->` |
| `<!-- @variable:source -->` | Variable source | `<!-- @variable:source:Step 1 Output -->` |

### UI Element Annotations

| Annotation | Purpose | Example |
|------------|---------|---------|
| `<!-- @ui:adaptivecard -->` | Adaptive Card definition | `<!-- @ui:adaptivecard -->` |
| `<!-- @ui:button -->` | Button definition | `<!-- @ui:button:Ping Assignee -->` |
| `<!-- @ui:input -->` | Input field | `<!-- @ui:input:TaskId -->` |

---

## File Structure

### 1. Topic Configuration Files (`topics/*.md`)
- Define Topics with triggers and actions
- Reference sub-agent files
- Include setup checklist

### 2. Sub-Agent System Prompt Files (`subagents/*-System-Prompt-Instructions.md`)
- Include flow annotations
- Include step definitions
- Include output formats

### 3. Sub-Agent Tool Configuration Files (`subagents/*-Tool-Configuration.md`)
- Include connector configurations
- Include action definitions
- Include parameter mappings

---

## Example: Complete Topic Definition

```markdown
# Morning Brief Topic

<!-- @topic:Morning_Brief -->
<!-- @topic:description:Daily briefing workflow - tasks + blockers -->
<!-- @topic:priority:1 -->

## Trigger Phrases
<!-- @trigger:morning brief -->
<!-- @trigger:run morning brief -->
<!-- @trigger:☀️ Run Morning Brief -->
<!-- @trigger:daily check -->
<!-- @trigger:what's blocked -->
<!-- @trigger:daily briefing -->

## Action
<!-- @action:agent:Morning_Brief_Agent -->

## Flow Definition

### Step 1: Get Tasks from Planner
<!-- @step:1 -->
<!-- @step:name:Get Tasks from Planner -->
<!-- @step:description:Retrieve all tasks from the project plan -->
<!-- @step:action:List tasks -->
<!-- @step:connector:Microsoft Planner -->
<!-- @step:parameters:PlanId={PlanId},Filter=Status ne 'completed' -->
<!-- @step:output:TasksList -->

### Step 2: Filter Overdue Tasks
<!-- @step:2 -->
<!-- @step:name:Filter Overdue Tasks -->
<!-- @step:description:Identify tasks overdue by 48+ hours -->
<!-- @step:action:Filter array -->
<!-- @step:condition:DueDate < Now - 48 hours -->
<!-- @step:output:OverdueTasks -->

### Step 3: Get Teams Messages
<!-- @step:3 -->
<!-- @step:name:Get Teams Messages -->
<!-- @step:description:Scan recent Teams messages for blockers -->
<!-- @step:action:Get messages -->
<!-- @step:connector:Microsoft Teams -->
<!-- @step:parameters:ChannelId={ChannelId},Top=50 -->
<!-- @step:output:MessagesList -->

### Step 4: Generate Summary
<!-- @step:4 -->
<!-- @step:name:Generate Summary -->
<!-- @step:description:Create Adaptive Card with morning brief -->
<!-- @step:action:Send response -->
<!-- @step:ui:adaptivecard -->

## Setup Checklist

- [ ] Create Topic: Morning_Brief
- [ ] Add Trigger Phrases (6 phrases)
- [ ] Add Agent Action: Morning_Brief_Agent
- [ ] Configure Connector: Microsoft Planner
- [ ] Configure Connector: Microsoft Teams
- [ ] Test Topic with "morning brief"
```

---

## Parser Tool

A Python script (`scripts/parse_topics.py`) can parse these enhanced markdown files and generate:
1. Setup checklists for Copilot Studio
2. JSON exports for automation
3. Validation reports

---

## Migration Guide

To convert existing markdown to enhanced format:

1. Add `<!-- @topic:TopicName -->` at the top
2. Add `<!-- @trigger:phrase -->` for each trigger phrase
3. Add `<!-- @action:agent:AgentName -->` for the action
4. Number workflow steps with `<!-- @step:N -->` annotations
5. Add setup checklist at the end
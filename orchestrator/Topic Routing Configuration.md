# Topic Routing Configuration

## Overview

This document defines the explicit Topic-based routing for the PM Agent system. The architecture uses 9 agents total:
- **1 Orchestrator** - Main user interface, routes to sub-agents
- **1 Knowledge Agent** - PM Operating Guide knowledge base
- **6 Workflow Agents** - Task-specific workflows
- **1 Fallback Agent** - Out-of-scope handling

**Architecture:**
- **Topics (6):** Core workflow flows that route to specific sub-agents
- **Routing:** Policy questions → Knowledge Agent, Tools → Workflow Agents

---

## Orchestration Mode

**Mode:** Standard (Topic-based)
**Reason:** DLP compliance - deterministic routing instead of AI-generated decisions

---

## Agent Mapping

| Agent | Purpose | Trigger |
|-------|---------|---------|
| **Knowledge Agent** | PM policy/governance questions | Policy questions |
| **Morning_Brief_Agent** | Daily brief workflow | Morning_Brief topic |
| **Friday_Wrap_Up_Agent** | Weekly wrap-up workflow | Friday_Wrap_Up topic |
| **Task_Review_Agent** | Task management | Task_Review topic |
| **Email_Triage_Agent** | Email scanning | Email_Triage topic |
| **Progress_Summary_Agent** | Progress reporting | Progress_Summary topic |
| **Governance_Action_Agent** | Teams posting | Governance_Action topic |
| **Fallback Agent** | Out-of-scope queries | No topic match |

---

## Core Workflow Topics

### Topic 1: Morning_Brief

**Purpose:** Execute Morning Brief workflow

| Trigger Phrases | Sub-Intent | Action |
|-----------------|------------|--------|
| "morning brief" | Run workflow | Call Morning_Brief_Agent |
| "run morning brief" | Execute flow | Call Morning_Brief_Agent |
| "☀️ Run Morning Brief" | Execute flow | Call Morning_Brief_Agent |
| "daily check" | Execute flow | Call Morning_Brief_Agent |
| "what's blocked" | Find blockers | Call Morning_Brief_Agent |
| "daily briefing" | Morning overview | Call Morning_Brief_Agent |

**Flow:** Morning_Brief_Agent coordinates:
1. Get tasks from Planner
2. Get messages from Teams
3. Identify overdue/stale tasks
4. Scan for blockers
5. Generate Adaptive Card

---

### Topic 2: Friday_Wrap_Up

**Purpose:** Execute Friday Wrap-Up workflow

| Trigger Phrases | Sub-Intent | Action |
|-----------------|------------|--------|
| "friday wrap-up" | Run workflow | Call Friday_Wrap_Up_Agent |
| "weekly wrap" | Execute flow | Call Friday_Wrap_Up_Agent |
| "📊 Generate Weekly Wrap" | Execute flow | Call Friday_Wrap_Up_Agent |
| "send weekly update" | Execute flow | Call Friday_Wrap_Up_Agent |
| "stakeholder report" | Execute flow | Call Friday_Wrap_Up_Agent |
| "end of week report" | Weekly summary | Call Friday_Wrap_Up_Agent |

**Flow:** Friday_Wrap_Up_Agent coordinates:
1. Get completed tasks (last 5 days)
2. Get current blockers
3. Generate Friday Wrap structure
4. Send via Outlook or Teams

---

### Topic 3: Task_Review

**Purpose:** Execute Task Review workflow

| Trigger Phrases | Sub-Intent | Action |
|-----------------|------------|--------|
| "check tasks" | List all tasks | Call Task_Review_Agent |
| "overdue tasks" | Find overdue tasks | Call Task_Review_Agent |
| "what tasks are due" | List tasks by due date | Call Task_Review_Agent |
| "task status" | Get task details | Call Task_Review_Agent |
| "how many tasks" | Count tasks | Call Task_Review_Agent |
| "check my tasks" | View task overview | Call Task_Review_Agent |
| "task summary" | Task overview | Call Task_Review_Agent |
| "create task" | Create new task | Call Task_Review_Agent |
| "assign task" | Assign task | Call Task_Review_Agent |
| "mark complete" | Complete task | Call Task_Review_Agent |

**Flow:** Task_Review_Agent coordinates:
1. List tasks from Planner
2. Categorize: Overdue, Stale, On Track
3. Execute task operations (create, update, complete)

---

### Topic 4: Email_Triage

**Purpose:** Execute Email Triage workflow

| Trigger Phrases | Sub-Intent | Action |
|-----------------|------------|--------|
| "check vendor updates" | Get vendor emails | Call Email_Triage_Agent |
| "check emails" | Get recent emails | Call Email_Triage_Agent |
| "vendor emails" | Filter vendor domain | Call Email_Triage_Agent |
| "any news from vendors" | Scan for updates | Call Email_Triage_Agent |
| "check for updates" | Email scan | Call Email_Triage_Agent |
| "email triage" | Process emails | Call Email_Triage_Agent |

**Flow:** Email_Triage_Agent coordinates:
1. Get emails from Outlook
2. Scan for keywords
3. Categorize by priority
4. Generate summary

---

### Topic 5: Progress_Summary

**Purpose:** Execute Progress Summary workflow

| Trigger Phrases | Sub-Intent | Action |
|-----------------|------------|--------|
| "progress summary" | Project progress | Call Progress_Summary_Agent |
| "project status" | Current status | Call Progress_Summary_Agent |
| "where are we" | Status overview | Call Progress_Summary_Agent |
| "how are we doing" | Health check | Call Progress_Summary_Agent |
| "project health" | Health assessment | Call Progress_Summary_Agent |
| "status report" | Generate report | Call Progress_Summary_Agent |

**Flow:** Progress_Summary_Agent coordinates:
1. Get task completion stats
2. Get active blockers
3. Get recent updates
4. Generate comprehensive summary

---

### Topic 6: Governance_Action

**Purpose:** Execute Governance Actions

| Trigger Phrases | Sub-Intent | Action |
|-----------------|------------|--------|
| "post risk alert" | Post to Teams | Call Governance_Action_Agent |
| "high risk" | Evaluate risk | Call Governance_Action_Agent |
| "risk escalation" | Escalate risk | Call Governance_Action_Agent |
| "post update" | Post to channel | Call Governance_Action_Agent |
| "notify team" | Team notification | Call Governance_Action_Agent |

**Flow:** Governance_Action_Agent coordinates:
1. Evaluate risk severity
2. Confirm before posting (for critical risks)
3. Post to Teams channel
4. Return confirmation

---

## Policy Questions: Knowledge Agent

**The following are NOT Topics** - they route to the Knowledge Agent:

| Question Type | Handler |
|---------------|---------|
| Budget escalation matrix | Knowledge Agent |
| Stale/overdue task policy | Knowledge Agent |
| PGOF stages/gates | Knowledge Agent |
| PCR/change request | Knowledge Agent |
| Contractor onboarding | Knowledge Agent |
| Pause/cancel project | Knowledge Agent |
| Financial tools (EPS, SIGMA, etc.) | Knowledge Agent |
| PCRA/Treasury Board | Knowledge Agent |
| Customer-Led vs SSC-Led | Knowledge Agent |
| Governance boards | Knowledge Agent |
| Vendor triage keywords | Knowledge Agent |
| Key terms and definitions | Knowledge Agent |
| Change management | Knowledge Agent |
| Risk escalation | Knowledge Agent |
| Enabling functions contact info | Knowledge Agent |
| Socio-economic priorities | Knowledge Agent |
| Lessons learned | Knowledge Agent |

---

## Fallback Handling

When no Topic matches:
1. Route to Fallback Agent
2. Fallback Agent evaluates if out-of-scope
3. If out-of-scope: Provide redirect guidance
4. If potentially in-scope: Offer disambiguation

---

## Suggested Prompts (Persistent Buttons)

Configure these as suggested prompts in Copilot Studio UI:

| Prompt | Action |
|--------|--------|
| ☀️ Run Morning Brief | Topic: Morning_Brief |
| 📊 Generate Weekly Wrap | Topic: Friday_Wrap_Up |
| 📧 Check Vendor Updates | Topic: Email_Triage |
| 📋 Check My Tasks | Topic: Task_Review |
| 📈 Progress Summary | Topic: Progress_Summary |
| 🚨 Post Risk Alert | Topic: Governance_Action |

---

## Topic Priority Order

When multiple Topics might match, Copilot Studio evaluates in this order:

1. **Morning_Brief** / **Friday_Wrap_Up** (workflows first)
2. **Task_Review** (task queries)
3. **Email_Triage** (email queries)
4. **Governance_Action** (Teams actions)
5. **Progress_Summary** (status queries)

---

## Architecture Diagram

```
User Query
    ↓
┌─────────────────────────────────────────────────┐
│  Orchestrator (System Prompt)                   │
│  - Knowledge Routing (Part A)                   │
│  - Tool Routing (Part B)                        │
│  - Guardrails (Part E)                          │
└─────────────────────────────────────────────────┘
    ↓
    ├──→ Policy Question? ──→ Knowledge Agent
    │
    └──→ Tool Request? ──→ Match to Topic
                                ↓
                    ┌─────────────────────────────┐
                    │ Topic Routing               │
                    │ - Morning_Brief             │
                    │ - Friday_Wrap_Up            │
                    │ - Task_Review               │
                    │ - Email_Triage              │
                    │ - Progress_Summary          │
                    │ - Governance_Action         │
                    └─────────────────────────────┘
                                ↓
                    ┌─────────────────────────────┐
                    │ Call Sub-Agent              │
                    │ (Planner/Outlook/Teams)     │
                    └─────────────────────────────┘
                                ↓
                    ┌─────────────────────────────┐
                    │ No Topic Match?             │
                    │ ──→ Fallback Agent          │
                    └─────────────────────────────┘
```

---

## Reference

- **Orchestrator System Prompt:** `orchestrator/Orchestrator System Prompt Instructions.md`
- **Knowledge Agent:** `orchestrator/Knowledge Agent - PM Operating Guide.md`
- **Sub-Agent Prompts:** `subagents/* - System Prompt Instructions.md`
- **Tool Config:** `subagents/* - Tool Configuration.md`
# Topic Routing Configuration

> **⚠️ IMPORTANT:** This is **reference documentation** with enhanced annotations for easy Copilot Studio Topic creation. Topics are configured directly in Copilot Studio UI.

<!-- @section:overview -->
## Overview

This document defines the Topic-based routing for the PM Agent system.

**Architecture:**
- **Topics:** Handle workflow routing (detect trigger phrases, call sub-agents)
- **Orchestrator:** Handles policy questions, fallback, and general conversation

---

## Orchestration Mode

**Mode:** Standard (Topic-based)
**Reason:** DLP compliance - deterministic routing instead of AI-generated decisions

---

## How Topics Work

All Topics are evaluated simultaneously when a user submits input. The first Topic with a matching trigger phrase "wins" and executes.

```
User Input
    ↓
Copilot Studio evaluates ALL Topics in priority order
    ↓
First Topic with matching trigger phrase → Calls its sub-agent
    ↓
No Topic matches → Orchestrator handles (policy question or fallback)
```

---

## Topic Configuration

<!-- @topic:Morning_Brief -->
### Topic 1: Morning_Brief

| Property | Value |
|----------|-------|
| **Name** | Morning_Brief |
| **Description** | Daily briefing workflow - tasks + blockers |
| **Priority** | 1 |

<!-- @trigger_list:start -->
**Trigger Phrases:**
<!-- @trigger:morning brief -->
- morning brief

<!-- @trigger:run morning brief -->
- run morning brief

<!-- @trigger:☀️ Run Morning Brief -->
- ☀️ Run Morning Brief

<!-- @trigger:daily check -->
- daily check

<!-- @trigger:what's blocked -->
- what's blocked

<!-- @trigger:daily briefing -->
- daily briefing
<!-- @trigger_list:end -->

<!-- @action:agent -->
**Action:** Call Agent: Morning_Brief_Agent

<!-- @connectors -->
**Required Connectors:** Microsoft Planner, Microsoft Teams

<!-- @setup_checklist -->
**Setup Checklist:**
- [ ] Create Topic: Morning_Brief
- [ ] Add Description: "Daily briefing workflow - tasks + blockers"
- [ ] Add Trigger Phrases (6 phrases listed above)
- [ ] Add Action: Call Agent → Morning_Brief_Agent
- [ ] Configure Connector: Microsoft Planner
- [ ] Configure Connector: Microsoft Teams
- [ ] Test with: "morning brief"

---

<!-- @topic:Friday_Wrap_Up -->
### Topic 2: Friday_Wrap_Up

| Property | Value |
|----------|-------|
| **Name** | Friday_Wrap_Up |
| **Description** | Weekly stakeholder report workflow |
| **Priority** | 2 |

<!-- @trigger_list:start -->
**Trigger Phrases:**
<!-- @trigger:friday wrap-up -->
- friday wrap-up

<!-- @trigger:weekly wrap -->
- weekly wrap

<!-- @trigger:📊 Generate Weekly Wrap -->
- 📊 Generate Weekly Wrap

<!-- @trigger:send weekly update -->
- send weekly update

<!-- @trigger:stakeholder report -->
- stakeholder report

<!-- @trigger:end of week report -->
- end of week report
<!-- @trigger_list:end -->

<!-- @action:agent -->
**Action:** Call Agent: Friday_Wrap_Up_Agent

<!-- @connectors -->
**Required Connectors:** Microsoft Planner, Microsoft Teams, Office 365 Outlook

<!-- @setup_checklist -->
**Setup Checklist:**
- [ ] Create Topic: Friday_Wrap_Up
- [ ] Add Description: "Weekly stakeholder report workflow"
- [ ] Add Trigger Phrases (6 phrases listed above)
- [ ] Add Action: Call Agent → Friday_Wrap_Up_Agent
- [ ] Configure Connector: Microsoft Planner
- [ ] Configure Connector: Microsoft Teams
- [ ] Configure Connector: Office 365 Outlook
- [ ] Test with: "friday wrap-up"

---

<!-- @topic:Task_Review -->
### Topic 3: Task_Review

| Property | Value |
|----------|-------|
| **Name** | Task_Review |
| **Description** | Task status and management |
| **Priority** | 3 |

<!-- @trigger_list:start -->
**Trigger Phrases:**
<!-- @trigger:check tasks -->
- check tasks

<!-- @trigger:overdue tasks -->
- overdue tasks

<!-- @trigger:what tasks are due -->
- what tasks are due

<!-- @trigger:task status -->
- task status

<!-- @trigger:how many tasks -->
- how many tasks

<!-- @trigger:assign task -->
- assign task

<!-- @trigger:reschedule task -->
- reschedule task

<!-- @trigger:mark complete -->
- mark complete

<!-- @trigger:create task -->
- create task

<!-- @trigger:check my tasks -->
- check my tasks

<!-- @trigger:task summary -->
- task summary
<!-- @trigger_list:end -->

<!-- @action:agent -->
**Action:** Call Agent: Task_Review_Agent

<!-- @connectors -->
**Required Connectors:** Microsoft Planner

<!-- @setup_checklist -->
**Setup Checklist:**
- [ ] Create Topic: Task_Review
- [ ] Add Description: "Task status and management"
- [ ] Add Trigger Phrases (11 phrases listed above)
- [ ] Add Action: Call Agent → Task_Review_Agent
- [ ] Configure Connector: Microsoft Planner
- [ ] Test with: "check tasks"

---

<!-- @topic:Email_Triage -->
### Topic 4: Email_Triage

| Property | Value |
|----------|-------|
| **Name** | Email_Triage |
| **Description** | Vendor email scanning and triage |
| **Priority** | 4 |

<!-- @trigger_list:start -->
**Trigger Phrases:**
<!-- @trigger:check vendor updates -->
- check vendor updates

<!-- @trigger:check emails -->
- check emails

<!-- @trigger:vendor emails -->
- vendor emails

<!-- @trigger:any news from vendors -->
- any news from vendors

<!-- @trigger:check for updates -->
- check for updates

<!-- @trigger:email triage -->
- email triage
<!-- @trigger_list:end -->

<!-- @action:agent -->
**Action:** Call Agent: Email_Triage_Agent

<!-- @connectors -->
**Required Connectors:** Office 365 Outlook

<!-- @setup_checklist -->
**Setup Checklist:**
- [ ] Create Topic: Email_Triage
- [ ] Add Description: "Vendor email scanning and triage"
- [ ] Add Trigger Phrases (6 phrases listed above)
- [ ] Add Action: Call Agent → Email_Triage_Agent
- [ ] Configure Connector: Office 365 Outlook
- [ ] Test with: "check vendor updates"

---

<!-- @topic:Progress_Summary -->
### Topic 5: Progress_Summary

| Property | Value |
|----------|-------|
| **Name** | Progress_Summary |
| **Description** | Project progress and health overview |
| **Priority** | 5 |

<!-- @trigger_list:start -->
**Trigger Phrases:**
<!-- @trigger:progress summary -->
- progress summary

<!-- @trigger:project status -->
- project status

<!-- @trigger:where are we -->
- where are we

<!-- @trigger:how are we doing -->
- how are we doing

<!-- @trigger:project health -->
- project health

<!-- @trigger:status report -->
- status report
<!-- @trigger_list:end -->

<!-- @action:agent -->
**Action:** Call Agent: Progress_Summary_Agent

<!-- @connectors -->
**Required Connectors:** Microsoft Planner, Microsoft Teams, Office 365 Outlook

<!-- @setup_checklist -->
**Setup Checklist:**
- [ ] Create Topic: Progress_Summary
- [ ] Add Description: "Project progress and health overview"
- [ ] Add Trigger Phrases (6 phrases listed above)
- [ ] Add Action: Call Agent → Progress_Summary_Agent
- [ ] Configure Connector: Microsoft Planner
- [ ] Configure Connector: Microsoft Teams
- [ ] Configure Connector: Office 365 Outlook
- [ ] Test with: "progress summary"

---

<!-- @topic:Governance_Action -->
### Topic 6: Governance_Action

| Property | Value |
|----------|-------|
| **Name** | Governance_Action |
| **Description** | Teams posting for risk alerts |
| **Priority** | 6 |

<!-- @trigger_list:start -->
**Trigger Phrases:**
<!-- @trigger:post risk alert -->
- post risk alert

<!-- @trigger:high risk -->
- high risk

<!-- @trigger:risk escalation -->
- risk escalation

<!-- @trigger:post update -->
- post update

<!-- @trigger:notify team -->
- notify team
<!-- @trigger_list:end -->

<!-- @action:agent -->
**Action:** Call Agent: Governance_Action_Agent

<!-- @connectors -->
**Required Connectors:** Microsoft Teams

<!-- @setup_checklist -->
**Setup Checklist:**
- [ ] Create Topic: Governance_Action
- [ ] Add Description: "Teams posting for risk alerts"
- [ ] Add Trigger Phrases (5 phrases listed above)
- [ ] Add Action: Call Agent → Governance_Action_Agent
- [ ] Configure Connector: Microsoft Teams
- [ ] Test with: "post risk alert"

---

## Orchestrator Role (Non-Topic)

The Orchestrator handles requests that don't match any Topic:

| Request Type | Handler | Action |
|--------------|---------|--------|
| Policy question | Orchestrator | Calls Knowledge Agent |
| Out of scope | Orchestrator | Calls Fallback Agent |
| General conversation | Orchestrator | Responds directly |

---

## Fallback Handling

When no Topic matches AND it's not a policy question:

1. Route to Fallback Agent
2. Fallback Agent evaluates if out-of-scope
3. If out-of-scope: Provide redirect guidance
4. If potentially in-scope: Offer disambiguation

---

## Suggested Prompts (Persistent Buttons)

Configure these as suggested prompts in Copilot Studio UI:

| Prompt | Topic | Action |
|--------|-------|--------|
| ☀️ Run Morning Brief | Morning_Brief | Trigger: "morning brief" |
| 📊 Generate Weekly Wrap | Friday_Wrap_Up | Trigger: "friday wrap-up" |
| 📧 Check Vendor Updates | Email_Triage | Trigger: "check vendor updates" |
| 📋 Check My Tasks | Task_Review | Trigger: "check tasks" |
| 📈 Progress Summary | Progress_Summary | Trigger: "progress summary" |
| 🚨 Post Risk Alert | Governance_Action | Trigger: "post risk alert" |

---

## Reference

- **Orchestrator System Prompt:** `orchestrator/Orchestrator System Prompt Instructions.md`
- **Knowledge Agent:** `orchestrator/Knowledge Agent - PM Operating Guide.md`
- **Sub-Agent Prompts:** `subagents/* - System Prompt Instructions.md`
- **Tool Config:** `subagents/* - Tool Configuration.md`
- **Enhanced Spec:** `docs/Enhanced-Markdown-Specification.md`

---

## Quick Setup Summary

| Topic | Priority | Trigger Count | Agent | Connectors |
|-------|----------|---------------|-------|------------|
| Morning_Brief | 1 | 6 | Morning_Brief_Agent | Planner, Teams |
| Friday_Wrap_Up | 2 | 6 | Friday_Wrap_Up_Agent | Planner, Teams, Outlook |
| Task_Review | 3 | 11 | Task_Review_Agent | Planner |
| Email_Triage | 4 | 6 | Email_Triage_Agent | Outlook |
| Progress_Summary | 5 | 6 | Progress_Summary_Agent | Planner, Teams, Outlook |
| Governance_Action | 6 | 5 | Governance_Action_Agent | Teams |
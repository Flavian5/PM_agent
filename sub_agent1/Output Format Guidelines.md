# Task & Schedule Specialist - Output Format Guidelines

## Response Structure

When returning task information to the Orchestrator, use the following structured format:

---

## Categorized Task List

### Format Template

```
1. CRITICAL/OVERDUE
   - [Task Name] - [Days Overdue] - [Assignee]
   - [Task Name] - [Days Overdue] - [Assignee]

2. STALE TASKS
   - [Task Name] - [Days In Progress] - [Assignee]
   - [Task Name] - [Days In Progress] - [Assignee]

3. ON TRACK
   - [Task Name] - [Due Date] - [Status]
   - [Task Name] - [Due Date] - [Status]
```

---

## Detailed Response Examples

### Example 1: Morning Brief Response

```
📋 TASK SPECIALIST REPORT - Morning Brief

🚨 CRITICAL/OVERDUE (2 tasks)
- API Integration - 3 days overdue - john.doe@company.com
- Database Migration - 2 days overdue - jane.smith@company.com

⚠️ STALE TASKS (1 task)
- Security Assessment - 7 days in progress - bob.wilson@company.com

✅ ON TRACK (5 tasks)
- Requirements Gathering - Due Mar 15 - In Progress
- Vendor Selection - Due Mar 20 - Not Started
- Test Plan Draft - Due Mar 18 - In Progress
```

### Example 2: Task Status Query

```
📊 Current Project Status

OVERDUE: 2 tasks requiring immediate attention
- [OVERDUE] Website Redesign - 5 days past due
- [OVERDUE] Client Demo Prep - 2 days past due

STALE: 1 task requiring update
- [STALE] Infrastructure Setup - 6 days in progress without update

HEALTHY: 8 tasks on track
```

### Example 3: Task Modification Confirmation

```
✅ Task Successfully Updated

Task: Website Redesign
Previous Due Date: March 5, 2026
New Due Date: March 12, 2026
Updated by: [User]
Status: Change confirmed
```

---

## Formatting Rules

### Critical Items (Overdue)
- Use 🚨 emoji prefix
- Use **[OVERDUE]** label in bold
- Include days overdue
- List assignee

### Warning Items (Stale)
- Use ⚠️ emoji prefix
- Use **[STALE]** label
- Include days in progress
- List assignee

### Normal Items (On Track)
- Use ✅ emoji prefix
- Show due date
- Show current status

---

## Adaptive Card Format (for Morning Brief)

When generating Adaptive Card for Orchestrator:

```json
{
  "type": "AdaptiveCard",
  "body": [
    {
      "type": "TextBlock",
      "text": "🚨 CRITICAL - Overdue Tasks",
      "weight": "bolder",
      "color": "attention"
    },
    {
      "type": "FactSet",
      "facts": [
        {"title": "API Integration", "value": "3 days overdue - john.doe@company.com"},
        {"title": "Database Migration", "value": "2 days overdue - jane.smith@company.com"}
      ]
    },
    {
      "type": "TextBlock",
      "text": "⚠️ STALE TASKS",
      "weight": "bolder",
      "color": "warning"
    },
    {
      "type": "FactSet",
      "facts": [
        {"title": "Security Assessment", "value": "7 days in progress - bob.wilson@company.com"}
      ]
    }
  ],
  "actions": [
    {
      "type": "Action.Execute",
      "title": "Ping Assignee",
      "verb": "pingAssignee",
      "data": {"taskId": "xxx", "assignee": "xxx"}
    },
    {
      "type": "Action.Execute",
      "title": "Reschedule for Tomorrow",
      "verb": "rescheduleTask",
      "data": {"taskId": "xxx", "newDate": "2026-03-11"}
    }
  ]
}
```

---

## Error Responses

### No Tasks Found
```
📭 No Tasks Found

No tasks were found in the specified Planner bucket. 
Please verify:
- The bucket ID is correct
- Tasks have been created in the board
- You are a member of the project board
```

### Access Denied
```
🔒 Access Denied

Unable to access the Planner board. 
Please ensure you are a member of the project board 
or contact your PRO Lead for access.
```

### Update Failed
```
❌ Update Failed

The task update could not be completed.
Please verify:
- Task ID is correct
- You have modify permissions
- New values are valid

Contact: pmcoe-cegp@ssc-spc.gc.ca for support
```

---

## Key Formatting Principles

1. **Consistent emoji usage**: 🚨 for critical, ⚠️ for warnings, ✅ for normal
2. **Bold labels**: Use **[OVERDUE]** and **[STALE]** for visibility
3. **Include assignee**: Always show who owns the task
4. **Provide context**: Show days overdue or in progress
5. **Actionable**: Recommend specific actions for each issue
# Task Review Agent - Tool Configuration

## Connected Services

| Service | Purpose | Operations Used |
|---------|---------|-----------------|
| **Microsoft Planner** | Task management | List tasks, Get task, Create task, Update task, Add comment |

---

## Tool Definitions

### Microsoft Planner

#### List Tasks
```
Action: listTasks
Description: Get all tasks from a specific Planner plan
Parameters:
  - planId (required): The Planner plan ID
  - $select: Optional OData query for filtering
  - $top: Maximum number of tasks to return (default: 50)
  - $orderby: Sort order (e.g., dueDateTime asc)
```

#### Get Task Details
```
Action: getTask
Description: Get detailed information about a specific task
Parameters:
  - taskId (required): The task ID
```

#### Create Task
```
Action: createTask
Description: Create a new task in a Planner plan
Parameters:
  - planId (required): The Planner plan ID
  - body (required): Task properties
    - title: Task title (required)
    - dueDateTime: ISO 8601 date (optional)
    - percentComplete: 0-100 (default: 0)
    - priority: 0-10 (optional, 0=urgent, 9=low)
    - assignedTo: User ID (optional)
    - description: Task description (optional)
```

#### Update Task
```
Action: updateTask
Description: Update task properties
Parameters:
  - taskId (required): The task ID
  - body (required): JSON object with updated properties
    - title: Task title
    - dueDateTime: ISO 8601 date
    - percentComplete: 0-100
    - priority: 0-10
    - assignedTo: User ID
    - bucketId: Bucket ID for organization
```

#### Add Comment
```
Action: addTaskComment
Description: Add a comment to a task
Parameters:
  - taskId (required): The task ID
  - body (required): Comment object
    - content: Comment text (required)
```

#### List Plans
```
Action: listPlans
Description: List Planner plans the user has access to
Parameters:
  - $top: Number of plans to return
```

---

## Configuration Notes

### Task Status Categories
Calculate categories based on:
- **Overdue:** currentDateTime - dueDateTime > 48 hours AND percentComplete < 100
- **Stale:** currentDateTime - lastModifiedDateTime > 5 business days AND percentComplete < 100
- **Due Soon:** dueDateTime - currentDateTime <= 3 days AND percentComplete < 100
- **On Track:** All other active tasks

### Priority Mapping
| Priority Value | Display |
|----------------|---------|
| 0 | 🔴 Urgent |
| 1-3 | 🟠 High |
| 4-6 | 🟡 Medium |
| 7-9 | 🟢 Low |

### Date Calculations
- Use business days for stale calculation (exclude weekends)
- Use calendar days for overdue calculation

---

## Error Responses

| Error | Message | Recovery Action |
|-------|---------|-----------------|
| Access Denied | "I don't have access to this plan" | List available plans |
| Not Found | "The task doesn't exist" | List tasks for selection |
| Validation Error | "Missing required field: [field]" | Prompt for missing field |
| Partial Failure | "Task updated but comment failed" | Show update confirmation |

---

## Output Format

Return results as Adaptive Card with:
1. **TextBlock** - Summary header with counts per category
2. **FactSet** - Tasks grouped by category
3. **ActionSet** - Action buttons (Complete, Reschedule, Reassign)

---

## Task Deletion Policy

**NEVER delete tasks.** If user requests deletion:
1. Explain: "I cannot delete tasks per PM policy"
2. Offer alternative: "Would you like me to mark it as canceled instead?"
3. If confirmed: Update title to include "CANCELED" and set percentComplete to 100
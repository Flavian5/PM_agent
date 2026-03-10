# Task & Schedule Specialist - Tool Configuration

## Connector: Microsoft Planner

### Actions to Enable

#### 1. List tasks
- **Purpose**: Fetch current task board state
- **When to use**: Every time user asks for task status, overdue items, or general overview
- **Parameters needed**:
  - Planner bucket ID (or list all buckets)
  - Task states (active, completed, all)
- **Safety level**: Read-only (no confirmation required)

#### 2. Update a task V2
- **Purpose**: Modify task status, due date, title, or assignment
- **When to use**: 
  - Mark task as completed
  - Change due date
  - Reassign task
  - Cancel task (add "CANCELED" to title)
- **Parameters needed**:
  - Task ID
  - Field to update (title, due date, percent complete, assigned to, bucket ID)
- **Safety level**: CONSEQUENTIAL - Requires user confirmation

---

## Safety Configuration

### Mark as Consequential
The following actions MUST be marked as "Require user confirmation" in Copilot Studio:

- **Update a task V2** - Any modification to task data
  - Reason: Task changes affect project tracking and reporting
  - UI: Display "Confirm" prompt before executing

### Recommended Settings

| Action | isConsequential | Require Confirmation |
|--------|-----------------|---------------------|
| List tasks | false | No |
| Update a task V2 | true | Yes (always) |

---

## Integration with Morning Brief Flow

### Flow: ☀️ Run Morning Brief

1. **Orchestrator** calls Task Specialist
2. **Task Specialist** executes "List tasks" to find:
   - Tasks overdue by 48+ hours (Critical/Overdue section)
   - Tasks in "In Progress" for 5+ days without comment (Stale section)
3. **Task Specialist** returns categorized list to Orchestrator
4. **Orchestrator** generates Adaptive Card with:
   - Red section: Overdue tasks
   - Yellow section: Stale tasks
   - Action buttons: [Ping Assignee], [Reschedule for Tomorrow]

### Action Button Mapping

| Button | Action | Tool |
|--------|--------|------|
| Ping Assignee | Post message to assignee in Teams | Teams: Post message in a chat or channel |
| Reschedule for Tomorrow | Update task due date | Planner: Update a task V2 |

---

## Error Handling

### Common Errors

1. **No tasks found**
   - Cause: Empty Planner bucket or wrong bucket ID
   - Response: "No tasks found in the specified Planner bucket. Please verify the bucket ID or check if tasks have been created."

2. **Access denied**
   - Cause: User not member of Planner board
   - Response: "Unable to access Planner. Please ensure you are a member of the project board."

3. **Update failed**
   - Cause: Invalid task ID or insufficient permissions
   - Response: "Task update failed. Please verify the task ID and your permissions."

---

## Best Practices

1. **Always list before updating** - Fetch current state before making changes
2. **Confirm each change** - Never auto-update; get user approval
3. **Provide context** - Include task name, current value, and proposed change in confirmation
4. **Validate dates** - Ensure new due dates are reasonable
5. **Document cancellations** - Add "CANCELED" to title AND include reason in comments
# Task Specialist - Tool Configuration

## Copilot Studio Connector: Microsoft Planner

### Exact Connector Name
**Microsoft Planner** (not to be confused with other planning tools)

### Actions to Enable

#### 1. List plans (FIND/RESOURCE DISCOVERY)
- **Copilot Studio Action Name**: `List plans` (under Microsoft Planner connector)
- **Purpose**: Find available Planner plans the user has access to
- **When to use**: When user doesn't specify a plan, or needs to choose which plan
- **Parameters needed**:
  - (none required - uses authenticated user's context)
- **Safety level**: Read-only (no confirmation required)

#### 2. Get plan (RESOURCE DETAIL)
- **Copilot Studio Action Name**: `Get plan` (under Microsoft Planner connector)
- **Purpose**: Get details of a specific plan including buckets and tasks
- **When to use**: When user selects a specific plan
- **Parameters needed**:
  - `PlanId` (the Planner plan ID)
- **Safety level**: Read-only (no confirmation required)

#### 3. List buckets (FIND/RESOURCE DISCOVERY)
- **Copilot Studio Action Name**: `List buckets` (under Microsoft Planner connector)
- **Purpose**: Find buckets within a specific plan
- **When to use**: When user wants to filter tasks by bucket
- **Parameters needed**:
  - `PlanId` (the Planner plan ID)
- **Safety level**: Read-only (no confirmation required)

#### 4. List tasks
- **Copilot Studio Action Name**: `List tasks` (under Microsoft Planner connector)
- **Purpose**: Fetch current task board state
- **When to use**: Every time user asks for task status, overdue items, or general overview
- **Parameters needed**:
  - `PlanId` (the Planner plan ID)
  - `BucketId` (optional - specific bucket)
  - `Top` (number of tasks to return, default 100)
- **Safety level**: Read-only (no confirmation required)

#### 5. Get task (RESOURCE DETAIL)
- **Copilot Studio Action Name**: `Get task` (under Microsoft Planner connector)
- **Purpose**: Get details of a specific task
- **When to use**: When user wants to see full task details
- **Parameters needed**:
  - `TaskId` (the Planner task ID)
- **Safety level**: Read-only (no confirmation required)

#### 6. Update a task V2
- **Copilot Studio Action Name**: `Update a task V2` (under Microsoft Planner connector)
- **Purpose**: Modify task status, due date, title, or assignment
- **When to use**: 
  - Mark task as completed
  - Change due date
  - Reassign task
  - Cancel task (add "CANCELED" to title)
- **Parameters needed**:
  - `TaskId` (the Planner task ID)
  - `Title` (optional - new title)
  - `DueDateTime` (optional - new due date)
  - `PercentComplete` (optional - 0-100)
  - `AssignedTo` (optional - user ID)
  - `BucketId` (optional - move to different bucket)
- **Safety level**: CONSEQUENTIAL - Requires user confirmation

---

## Safety Configuration

### Mark as Consequential
The following actions MUST be marked as "Require user confirmation" in Copilot Studio:

- **Update a task V2** - Any modification to task data
  - Reason: Task changes affect project tracking and reporting
  - UI: Display "Confirm" prompt before executing

### Recommended Settings

| Action | Connector | isConsequential | Require Confirmation |
|--------|-----------|-----------------|---------------------|
| List tasks | Microsoft Planner | false | No |
| Update a task V2 | Microsoft Planner | true | Yes (always) |

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

| Button | Action | Connector | Tool |
|--------|--------|-----------|------|
| Ping Assignee | Post message to assignee in Teams | Microsoft Teams | Post message in a chat or channel |
| Reschedule for Tomorrow | Update task due date | Microsoft Planner | Update a task V2 |

---

## Error Handling

### Common Errors

1. **No tasks found**
   - Cause: Empty Planner bucket or wrong Plan ID
   - Response: "No tasks found in the specified Planner bucket. Please verify the Plan ID or check if tasks have been created."

2. **Access denied**
   - Cause: User not member of Planner plan
   - Response: "Unable to access Planner. Please ensure you are a member of the project plan."

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
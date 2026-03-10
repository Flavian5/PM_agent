# Morning Brief Agent - Tool Configuration

## Connected Services

| Service | Purpose | Operations Used |
|---------|---------|-----------------|
| **Microsoft Planner** | Task management | List tasks, Get task details, Update task |
| **Microsoft Teams** | Team communication | Get messages, Send message |

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
```

#### Get Task Details
```
Action: getTask
Description: Get detailed information about a specific task
Parameters:
  - taskId (required): The task ID
```

#### Update Task
```
Action: updateTask
Description: Update task properties (status, due date, assignee)
Parameters:
  - taskId (required): The task ID
  - body (required): JSON object with updated properties
    - percentComplete: 0-100
    - dueDateTime: ISO 8601 date
    - assignedTo: User ID
    - title: Task title
```

---

### Microsoft Teams

#### Get Recent Messages
```
Action: getMessages
Description: Get recent messages from a Teams channel
Parameters:
  - teamId (required): The Teams team ID
  - channelId (required): The channel ID
  - $top: Number of messages (default: 20)
  - $filter: OData filter for date range
```

#### Send Message
```
Action: sendMessage
Description: Send a message to a Teams channel or chat
Parameters:
  - teamId (required): The Teams team ID (for channel messages)
  - channelId (required): The channel ID (for channel messages)
  - body (required): Message content
    - content: Message text (HTML supported)
    - subject: Optional subject line
```

#### List Teams
```
Action: listTeams
Description: List Teams the user has access to
Parameters:
  - $top: Number of teams to return
```

#### List Channels
```
Action: listChannels
Description: List channels in a specific Team
Parameters:
  - teamId (required): The Teams team ID
```

---

## Configuration Notes

### Plan/Team Selection
- If user has access to only one plan: Use it automatically
- If user has access to multiple plans: Ask user to select
- Store selection in session for future requests

### Message Scanning Keywords
Configure these as scan targets:
- "blocked" → Priority 1 (Critical)
- "urgent" → Priority 1 (Critical)
- "help" → Priority 2 (High)
- "issue" → Priority 2 (High)
- "stuck" → Priority 2 (High)
- "waiting on" → Priority 3 (Medium)

### Date Calculations
- **Overdue:** Current time - dueDateTime > 48 hours
- **Stale:** Current time - lastModifiedDateTime > 5 business days
- **Due Today:** dueDateTime is within today
- **Upcoming:** dueDateTime is within next 3 days

---

## Error Responses

| Error | Message | Recovery Action |
|-------|---------|-----------------|
| Access Denied | "I don't have access to this plan/channel" | List available resources |
| Not Found | "The plan or channel doesn't exist" | Ask user to verify ID |
| Rate Limited | "Too many requests, please wait" | Retry after 30 seconds |
| Partial Failure | "Got tasks but no messages" | Show partial results |

---

## Output Format

Return results as Adaptive Card with:
1. **Container** (vertical layout)
2. **TextBlock** - Section headers
3. **FactSet** - Task/blocker details
4. **ActionSet** - Action buttons
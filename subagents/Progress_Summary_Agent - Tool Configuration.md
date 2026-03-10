# Progress Summary Agent - Tool Configuration

## Connected Services

| Service | Purpose | Operations Used |
|---------|---------|-----------------|
| **Microsoft Planner** | Task management | List tasks, Get task details |
| **Microsoft Teams** | Team communication | Get messages |
| **Microsoft Outlook** | Email management | Get emails |

---

## Tool Definitions

### Microsoft Planner

#### List Tasks
```
Action: listTasks
Description: Get all tasks from a specific Planner plan
Parameters:
  - planId (required): The Planner plan ID
  - $top: Maximum number of tasks to return (default: 100)
```

#### Get Task Details
```
Action: getTask
Description: Get detailed information about a specific task
Parameters:
  - taskId (required): The task ID
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
  - $top: Number of messages (default: 50)
  - $filter: OData filter for date range (last 14 days)
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

### Microsoft Outlook

#### Get Emails
```
Action: getEmails
Description: Get recent emails from user's inbox
Parameters:
  - $filter: OData filter for date range (last 7 days)
  - $top: Number of emails to return (default: 20)
  - $orderby: Sort order (receivedDateTime desc)
```

#### Send Email
```
Action: sendEmail
Description: Send an email to stakeholders
Parameters:
  - message (required): Email message object
    - subject: Email subject line
    - body: Email content (HTML supported)
    - toRecipients: Array of email addresses
    - saveToSentItems: Boolean (default: true)
```

---

## Configuration Notes

### Task Statistics Calculation
Calculate completion metrics:
- **Total:** Count of all tasks
- **Completed:** percentComplete = 100
- **In Progress:** 0 < percentComplete < 100
- **Not Started:** percentComplete = 0
- **Completion %:** (Completed / Total) * 100

### Health Assessment Rules
| Condition | Status | Color |
|-----------|--------|-------|
| No blockers AND >70% complete | On Track | 🟢 Green |
| No blockers AND 40-70% complete | At Risk | 🟡 Yellow |
| Any blockers AND <40% complete | Critical | 🔴 Red |
| High/High risks in EPS | Critical | 🔴 Red |

### Blocker Detection Keywords
- "blocked"
- "waiting on"
- "issue"
- "stuck"
- "problem"
- "delayed"

### Milestone Identification
Identify tasks with:
- Due date within next 30 days
- percentComplete < 100 (not completed)
- Priority 0-1 (high priority)

---

## Error Responses

| Error | Message | Recovery Action |
|-------|---------|-----------------|
| Access Denied | "I don't have access to [resource]" | List available resources |
| Not Found | "The plan/channel doesn't exist" | Ask user to verify |
| Partial Failure | "Got tasks but no messages" | Show partial results |

---

## Output Format

Return results as Adaptive Card with:
1. **TextBlock** - Health indicator (colored), completion %
2. **FactSet** - Task breakdown (Completed, In Progress, Not Started)
3. **FactSet** - Current blockers
4. **FactSet** - Recent updates
5. **FactSet** - Upcoming milestones
6. **ActionSet** - Action buttons (Generate Report, Send, Post, View Tasks)
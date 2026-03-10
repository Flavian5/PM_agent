# Friday Wrap-Up Agent - Tool Configuration

## Connected Services

| Service | Purpose | Operations Used |
|---------|---------|-----------------|
| **Microsoft Planner** | Task management | List tasks, Get task details |
| **Microsoft Teams** | Team communication | Get messages |
| **Microsoft Outlook** | Email delivery | Send email |

---

## Tool Definitions

### Microsoft Planner

#### List Tasks
```
Action: listTasks
Description: Get all tasks from a specific Planner plan
Parameters:
  - planId (required): The Planner plan ID
  - $filter: Filter for completed tasks (percentComplete eq 100)
  - $top: Maximum number of tasks to return (default: 50)
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
  - $filter: OData filter for date range (last 7 days)
```

---

### Microsoft Outlook

#### Send Email
```
Action: sendEmail
Description: Send an email to stakeholders
Parameters:
  - message (required): Email message object
    - subject: Email subject line
    - body: Email content (HTML supported)
    - toRecipients: Array of email addresses
    - ccRecipients: Optional CC recipients
    - saveToSentItems: Boolean (default: true)
```

#### Get Distribution Lists
```
Action: getDistributionLists
Description: Get available distribution lists for the organization
Parameters:
  - $top: Number of lists to return
```

---

## Configuration Notes

### Date Range Calculation
- **Last 5 business days:** Exclude weekends from date calculation
- **Last 7 days:** Include last 7 calendar days for Teams messages

### Blocker Detection Keywords
Configure these as scan targets:
- "blocked" → Include in blockers
- "waiting on" → Include in blockers
- "issue" → Include in blockers
- "stuck" → Include in blockers
- "resolved" → Exclude from blockers (mark as resolved)

### Stakeholder List
- If user has a saved stakeholder list: Use it automatically
- If not: Ask user for email addresses or distribution list name

### Report Customization Toggles
- **Include Next Week:** Add "Next Week's Focus" section
- **Highlight Risks:** Bold and add 🚨 emoji to blockers

---

## Error Responses

| Error | Message | Recovery Action |
|-------|---------|-----------------|
| Access Denied | "I don't have access to this plan/channel" | List available resources |
| Not Found | "The plan or channel doesn't exist" | Ask user to verify ID |
| Email Failed | "Failed to send email" | Show draft for manual send |
| Partial Failure | "Got tasks but no messages" | Show partial results |

---

## Output Format

Return results as Adaptive Card with:
1. **Container** (vertical layout)
2. **TextBlock** - Executive summary
3. **FactSet** - Completed tasks
4. **FactSet** - Blockers
5. **FactSet** - Next week focus
6. **ActionSet** - Action buttons (Edit, Send, Post)
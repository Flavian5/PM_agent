# Governance Action Agent - Tool Configuration

## Connected Services

| Service | Purpose | Operations Used |
|---------|---------|-----------------|
| **Microsoft Teams** | Team communication | Get messages, Send message, List teams, List channels |

---

## Tool Definitions

### Microsoft Teams

#### List Teams
```
Action: listTeams
Description: List Teams the user has access to
Parameters:
  - $top: Number of teams to return (default: 50)
```

#### List Channels
```
Action: listChannels
Description: List channels in a specific Team
Parameters:
  - teamId (required): The Teams team ID
```

#### Get Messages
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

#### Send Chat Message
```
Action: sendChatMessage
Description: Send a direct message to a user
Parameters:
  - chatId: The chat ID (for 1:1 messages)
  - body (required): Message content
    - content: Message text
```

---

## Configuration Notes

### Risk Severity Assessment
| Impact | Probability | Severity | Emoji |
|--------|-------------|----------|-------|
| High | High | CRITICAL | 🚨 |
| High | Low | ELEVATED | ⚠️ |
| Low | High | ELEVATED | ⚠️ |
| Low | Low | LOW | 🟢 |

### Confirmation Requirements
- **CRITICAL risks:** ALWAYS require explicit confirmation before posting
- **ELEVATED risks:** Require confirmation before posting
- **LOW risks:** Can post without confirmation but should inform user

### Channel Selection
- If user specifies channel: Use that channel
- If user doesn't specify: Ask user to select from available channels
- Store selection in session for future requests

### Message Formatting
Use HTML formatting for Teams messages:
- Bold: `<strong>text</strong>`
- Italic: `<em>text</em>`
- Lists: `<ul><li>item</li></ul>`
- Line breaks: `<br>`

---

## Error Responses

| Error | Message | Recovery Action |
|-------|---------|-----------------|
| Access Denied | "I don't have access to Teams" | Request permissions |
| Not Found | "The team or channel doesn't exist" | List available resources |
| Send Failed | "Failed to post message" | Retry or show draft |
| Rate Limited | "Too many requests" | Retry after 30 seconds |

---

## Output Format

Return results as Adaptive Card with:
1. **TextBlock** - Risk assessment summary with severity color
2. **FactSet** - Risk details (Description, Impact, Probability, Owner)
3. **ActionSet** - Action buttons (Post, Confirm, Cancel)

---

## Special Handling

### High/High Risk (Critical)
Per PM policy: "Any risk with High Impact + High Probability: Post alert to Teams channel"
1. Always confirm before posting
2. Use 🚨 emoji in subject
3. Include "Recommended Action" field
4. Suggest creating follow-up task

### Risk Escalation
When user says "escalate risk":
1. Confirm it's intentional
2. Post to higher-visibility channel (if multiple)
3. Include PMB in notification (if applicable)
4. Create tracking task in Planner
# Risk Specialist - Tool Configuration

## Copilot Studio Connector: Microsoft Teams

### Exact Connector Name
**Microsoft Teams** (not to be confused with "Teams for Business" or other variants)

### Actions to Enable

#### 1. Get messages
- **Copilot Studio Action Name**: `Get messages` (under Microsoft Teams connector)
- **Purpose**: Scan project channel for keywords like "blocked" or "help"
- **When to use**: 
  - Morning Brief flow - scan for blockers
  - User asks about project channel activity
  - Identify active risks and issues
- **Parameters needed**:
  - `TeamId` (the Teams team ID)
  - `ChannelId` (the Teams channel ID)
  - `Top` (number of messages to return, default 50)
  - `Skip` (optional - for pagination)
- **Safety level**: Read-only (no confirmation required)

**Note**: To search for specific keywords, you can use the `Filter` parameter or process results after retrieval.

#### 2. Post message in a chat or channel
- **Copilot Studio Action Name**: `Post message in a chat or channel` (under Microsoft Teams connector)
- **Purpose**: Post risk alerts, governance notifications, project updates
- **When to use**: 
  - High Impact + High Probability risk identified
  - User confirms posting risk alert
  - Governance notification required
- **Parameters needed**:
  - `ChatId` OR `ChannelId` (where to post)
  - `TeamId` (required for channel posts)
  - `Message` (message content - can be HTML or plain text)
  - `Subject` (optional - for channel posts)
- **Safety level**: CONSEQUENTIAL - Requires user confirmation

---

## Safety Configuration

### Mark as Consequential
The following actions MUST be marked as "Require user confirmation" in Copilot Studio:

- **Post message in a chat or channel** - Any posting action
  - Reason: Messages go to project stakeholders; must verify content
  - UI: Display "Confirm" prompt before posting
  - Always ask: *"Shall I post a risk alert to the Teams channel?"*

### Recommended Settings

| Action | Connector | isConsequential | Require Confirmation |
|--------|-----------|-----------------|---------------------|
| Get messages | Microsoft Teams | false | No |
| Post message in a chat or channel | Microsoft Teams | true | Yes (always) |

---

## Integration with Flows

### Flow 1: Morning Brief (Teams Scan)

1. **Orchestrator** calls Risk Specialist
2. **Risk Specialist** executes "Get messages" to scan project channel:
   - TeamId: [project team ID]
   - ChannelId: [project channel ID]
   - Top: 50 (or as needed)
3. **Risk Specialist** searches for keywords:
   - "blocked"
   - "help"
   - "issue"
   - "problem"
   - "risk"
   - "urgent"
4. **Risk Specialist** returns summarized blockers to Orchestrator
5. **Orchestrator** generates Adaptive Card with:
   - Red section: Blockers from Teams
   - Action buttons: [Post Alert], [Create Task]

### Flow 2: Risk Escalation

1. **User** describes a risk: "We might miss the deadline due to vendor delay"
2. **Risk Specialist** evaluates:
   - Impact: High/Medium/Low
   - Probability: High/Medium/Low
3. **If High Impact + High Probability**:
   - Risk Specialist asks: *"Shall I post a risk alert to the Teams channel?"*
   - User confirms
   - Risk Specialist executes "Post message in a chat or channel" with:
     - TeamId: [project team ID]
     - ChannelId: [project channel ID]
     - Message: Risk alert content
4. **If not High/High**:
   - Risk Specialist provides guidance on mitigation

### Flow 3: Governance Questions

1. **User** asks policy question
2. **Risk Specialist** answers directly from embedded SOPs
3. **If escalation needed**:
   - Risk Specialist explains approval threshold
   - Recommends next steps

---

## Risk Evaluation Logic

### Escalation Criteria

| Impact | Probability | Action |
|--------|-------------|--------|
| High | High | **IMMEDIATE** - Post to Teams, notify Sponsor |
| High | Medium | Elevate to PM, document in EPS |
| Medium | High | Document in EPS, monitor closely |
| Medium | Medium | Document in EPS, regular review |
| Low | Any | Document in EPS, routine monitoring |

### Budget Variance Response

| Variance | Response |
|----------|----------|
| < $1,000 | "PM can auto-approve" |
| $1,000 - $5,000 | "Requires PM Manager approval" |
| > $5,000 | "Requires Project Sponsor approval" |
| > 10% baseline | "Requires Project Sponsor approval" |
| SSC-Led + increase | "Requires FIMB + PMB approval" |

---

## Error Handling

### Common Errors

1. **No messages found**
   - Cause: Empty channel or wrong Team/Channel ID
   - Response: "No recent messages found in the project channel. The channel may be empty or the Team/Channel ID may be incorrect."

2. **Access denied**
   - Cause: Not member of team/channel
   - Response: "Unable to access the Teams channel. Please verify you are a member of the project team."

3. **Post failed**
   - Cause: No posting permissions or channel locked
   - Response: "Message could not be posted. Please verify your permissions and try again."

---

## Best Practices

1. **Always evaluate risk** - Determine Impact and Probability before escalating
2. **Confirm before posting** - Never auto-post to Teams; get user approval
3. **Answer from knowledge** - Use embedded SOPs, don't refer to external documents
4. **Include thresholds** - When discussing budgets, always mention approval levels
5. **Reference embedded knowledge** - Cite specific SOPs when answering policy questions
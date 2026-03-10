# Vendor & Communications Specialist - Tool Configuration

## Connector: Office 365 Outlook

### Actions to Enable

#### 1. Get emails (V3)
- **Purpose**: Fetch recent emails from vendor domains
- **When to use**: 
  - User asks "Check for vendor updates"
  - User asks to review recent communications
  - Morning Brief flow - vendor email check
- **Parameters needed**:
  - Folder (usually Inbox)
  - Filter for sender domains (vendor domains)
  - Date range (last 7 days default)
  - Unread only option
- **Safety level**: Read-only (no confirmation required)

#### 2. Send an email (V2)
- **Purpose**: Send stakeholder reports, Friday Wrap-Up, notifications
- **When to use**: 
  - User confirms sending Friday Wrap-Up
  - User confirms sending stakeholder update
  - User confirms sending notification
- **Parameters needed**:
  - To recipients
  - Subject line
  - Body content
  - Attachments (if any)
- **Safety level**: CONSEQUENTIAL - Requires user confirmation

---

## Safety Configuration

### Mark as Consequential
The following actions MUST be marked as "Require user confirmation" in Copilot Studio:

- **Send an email (V2)** - Any email sending action
  - Reason: Emails go to external stakeholders; must verify recipients and content
  - UI: Display "Confirm" prompt before sending
  - Option: Save as draft instead of immediate send

### Recommended Settings

| Action | isConsequential | Require Confirmation |
|--------|-----------------|---------------------|
| Get emails (V3) | false | No |
| Send an email (V2) | true | Yes (always) |

---

## Integration with Flows

### Flow 1: Vendor & Communications Triage

1. **User** types: "Check for vendor updates"
2. **Orchestrator** delegates to Comms Specialist
3. **Comms Specialist** executes "Get emails (V3)" with filters:
   - Unread messages
   - Vendor domains (configurable)
   - Last 7 days
4. **Comms Specialist** scans for keywords:
   - delayed, invoice, shipped, blocked, issue, ETA
5. **Comms Specialist** returns summarized updates (max 3 bullets each)
6. **Orchestrator** generates Adaptive Card with:
   - Synthesized vendor updates
   - Dropdown menus to assign team members
   - [Add as Tasks to Planner] button

### Flow 2: Friday Wrap-Up

1. **User** clicks: [📊 Generate Weekly Wrap]
2. **Orchestrator** coordinates with Task Specialist for completed tasks
3. **Orchestrator** coordinates with Risk Specialist for blockers
4. **Comms Specialist** generates Friday Wrap-Up structure:
   - Executive Summary
   - Completed Milestones
   - Current Blockers
   - Next Week's Focus
5. **Orchestrator** generates "Email Preview" Adaptive Card with:
   - Editable text block
   - Toggle switches: [Include Next Week's Goals], [Highlight Risks]
   - [Send Update to Stakeholders] button
6. **User** clicks [Send Update to Stakeholders]
7. **Comms Specialist** executes "Send an email (V2)" (requires confirmation)

---

## Keyword Scanning Logic

### Priority Keywords (Critical)
| Keyword | Action | Category |
|---------|--------|----------|
| delayed | Flag as critical | 🔴 CRITICAL |
| blocked | Flag as critical | 🔴 CRITICAL |
| issue | Flag as critical | 🔴 CRITICAL |
| invoice | Flag with warning | ⚠️ INVOICES |

### Standard Keywords (Updates)
| Keyword | Action | Category |
|---------|--------|----------|
| shipped | Include in updates | 🟢 SHIPPED |
| ETA | Include in updates | 🟡 UPDATES |
| delivered | Include in updates | 🟢 DELIVERED |

---

## Error Handling

### Common Errors

1. **No emails found**
   - Cause: No unread emails from vendor domains
   - Response: "No unread vendor updates found. Try expanding the search to all emails or a longer date range."

2. **Access denied**
   - Cause: Insufficient Outlook permissions
   - Response: "Unable to access Outlook. Please verify your email permissions."

3. **Send failed**
   - Cause: Invalid recipients or server issue
   - Response: "Email could not be sent. Please verify recipient addresses and try again."

---

## Best Practices

1. **Never output full email bodies** - Summarize in max 3 bullets
2. **Always flag invoices** - Add Accounts Payable warning
3. **Confirm before sending** - Never auto-send stakeholder communications
4. **Use draft option** - Recommend saving as draft for user review
5. **Include toggle options** - Let user choose what to include in reports
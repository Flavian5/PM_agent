# Comms Specialist - Tool Configuration

## Copilot Studio Connector: Office 365 Outlook

### Exact Connector Name
**Office 365 Outlook** (not to be confused with "Outlook.com" or other email connectors)

### Actions to Enable

#### 1. Get messages (FIND/RESOURCE DISCOVERY)
- **Copilot Studio Action Name**: `Get messages` (under Office 365 Outlook connector)
- **Purpose**: Find/recent emails in the user's mailbox
- **When to use**: When user doesn't specify filters, or to list recent emails
- **Parameters needed**:
  - `Folder` (usually "Inbox")
  - `Top` (number of emails to return, default 50)
  - `Skip` (optional - for pagination)
- **Safety level**: Read-only (no confirmation required)

#### 2. Get emails (V3)
- **Copilot Studio Action Name**: `Get emails (V3)` (under Office 365 Outlook connector)
- **Purpose**: Fetch recent emails from vendor domains with filtering
- **When to use**: 
  - User asks "Check for vendor updates"
  - User asks to review recent communications
  - Morning Brief flow - vendor email check
- **Parameters needed**:
  - `Folder` (usually "Inbox")
  - `Filter` (optional - OData filter for sender address)
  - `Top` (number of emails to return, default 50)
  - `Skip` (optional - for pagination)
- **Safety level**: Read-only (no confirmation required)

**Note**: To filter by vendor domains, use the `Filter` parameter with OData syntax:
```
from/emailAddress/address eq 'vendor@domain.com'
```
Or use `Search` parameter for keyword searches.

#### 3. Get message (RESOURCE DETAIL)
- **Copilot Studio Action Name**: `Get message` (under Office 365 Outlook connector)
- **Purpose**: Get full details of a specific email
- **When to use**: When user wants to read full email content
- **Parameters needed**:
  - `Id` (the message ID)
- **Safety level**: Read-only (no confirmation required)

#### 4. Send an email (V2)
- **Copilot Studio Action Name**: `Send an email (V2)` (under Office 365 Outlook connector)
- **Purpose**: Send stakeholder reports, Friday Wrap-Up, notifications
- **When to use**: 
  - User confirms sending Friday Wrap-Up
  - User confirms sending stakeholder update
  - User confirms sending notification
- **Parameters needed**:
  - `To` (recipient email addresses, semicolon separated)
  - `Subject` (email subject line)
  - `Body` (email body content - HTML or plain text)
  - `CC` (optional - carbon copy recipients)
  - `BCC` (optional - blind carbon copy recipients)
  - `Attachments` (optional - file attachments)
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

| Action | Connector | isConsequential | Require Confirmation |
|--------|-----------|-----------------|---------------------|
| Get emails (V3) | Office 365 Outlook | false | No |
| Send an email (V2) | Office 365 Outlook | true | Yes (always) |

---

## Integration with Flows

### Flow 1: Vendor & Communications Triage

1. **User** types: "Check for vendor updates"
2. **Orchestrator** delegates to Comms Specialist
3. **Comms Specialist** executes "Get emails (V3)" with filters:
   - Folder: Inbox
   - Filter: Vendor domain(s) - configure specific domains per project
   - Top: 50 (or as needed)
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
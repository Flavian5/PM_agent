# Email Triage Agent - Tool Configuration

## Connected Services

| Service | Purpose | Operations Used |
|---------|---------|-----------------|
| **Microsoft Outlook** | Email management | Get emails, Send email, Mark as read, Flag email |

---

## Tool Definitions

### Microsoft Outlook

#### Get Emails
```
Action: getEmails
Description: Get recent emails from user's inbox
Parameters:
  - $filter: OData filter for date range
  - $top: Number of emails to return (default: 20)
  - $select: Specific fields to return
  - $orderby: Sort order (e.g., receivedDateTime desc)
```

#### Get Email Details
```
Action: getEmail
Description: Get detailed information about a specific email
Parameters:
  - messageId (required): The message ID
```

#### Send Email
```
Action: sendEmail
Description: Send an email
Parameters:
  - message (required): Email message object
    - subject: Email subject line
    - body: Email content (HTML supported)
    - toRecipients: Array of email addresses
    - ccRecipients: Optional CC recipients
    - saveToSentItems: Boolean (default: true)
```

#### Mark as Read
```
Action: markAsRead
Description: Mark an email as read
Parameters:
  - messageId (required): The message ID
```

#### Flag Email
```
Action: flagEmail
Description: Flag an email for follow-up
Parameters:
  - messageId (required): The message ID
  - flagStatus: "flagged" or "unflagged"
  - dueDateTime: Optional reminder date
```

#### Forward Email
```
Action: forwardEmail
Description: Forward an email to another recipient
Parameters:
  - messageId (required): The message ID
  - body: Optional message to add
  - recipients: Array of email addresses to forward to
```

---

## Configuration Notes

### Date Range Options
| Option | Filter |
|--------|--------|
| Last 24 hours | receivedDateTime ge [24h ago] |
| Last 7 days | receivedDateTime ge [7d ago] |
| Last 30 days | receivedDateTime ge [30d ago] |

### Keyword Scanning Rules
Configure these keywords for categorization:

**CRITICAL (Action Required):**
- delayed
- blocked
- issue
- urgent
- help
- stuck
- problem
- critical

**WARNING (Finance):**
- invoice
- payment
- billing
- PO number

**UPDATE (Shipping):**
- shipped
- delivered
- tracking
- arrived

**INFO (General):**
- meeting
- calendar
- invite
- reminder

### Vendor Domain Filtering
If user requests vendor-specific updates, filter by known vendor domains:
- Extract domain from sender email
- Match against known vendor list
- Prioritize emails from vendor domains

---

## Error Responses

| Error | Message | Recovery Action |
|-------|---------|-----------------|
| Access Denied | "I don't have access to your emails" | Request permissions |
| Not Found | "The email doesn't exist" | Show recent emails |
| Send Failed | "Failed to send email" | Show draft for manual send |
| Rate Limited | "Too many requests" | Retry after 30 seconds |

---

## Output Format

Return results as Adaptive Card with:
1. **TextBlock** - Summary header with counts per category
2. **FactSet** - Emails grouped by priority
3. **ActionSet** - Action buttons (Mark Read, Flag, Reply, Forward)

---

## Invoice Handling Special Case

When email contains "invoice" keyword:
1. Do NOT process or approve
2. Flag with warning: "⚠️ PM Action Required: Route to Accounts Payable"
3. Offer "Route to Finance" action button
4. Do not include in regular summary - highlight separately
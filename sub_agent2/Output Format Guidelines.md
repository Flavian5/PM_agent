# Vendor & Communications Specialist - Output Format Guidelines

## Response Structure

When returning communication data to the Orchestrator, use the following structured formats:

---

## Vendor Triage Response Format

### Template
```
📧 VENDOR UPDATE SUMMARY

🔴 CRITICAL (Immediate Action)
• [Vendor Name] - [Brief summary of critical issue]
• [Vendor Name] - [Brief summary of delay]

🟡 STANDARD UPDATES
• [Vendor Name] - [Summary]
• [Vendor Name] - [Summary]

🟢 SHIPPED/DELIVERED
• [Vendor Name] - [Delivery confirmation]

⚠️ INVOICES DETECTED
• [Vendor Name] - [Invoice summary]
  → PM Action Required: Route to Accounts Payable via standard finance portal
```

---

## Detailed Examples

### Example 1: Vendor Email Triage

```
📧 VENDOR UPDATE SUMMARY - March 10, 2026

🔴 CRITICAL (2)
• Acme Corp - "API Integration Delayed" - Project blocked, waiting on credentials
• TechSupply - "Hardware Shipment Issue" - Damaged goods, replacement required

🟡 UPDATES (3)
• CloudServices Inc - "Monthly Usage Report" - Within expected parameters
• DataSync Ltd - "Migration Status" - On track for March 15 completion
• SecurityPro - "License Renewal" - Renewal due in 30 days

🟢 SHIPPED (1)
• HardwareExpress - "Server Delivery" - Arrived March 8, signed for

⚠️ INVOICES (1)
• Acme Corp - "Invoice #2026-0342" - $15,000
  → PM Action Required: Route to Accounts Payable via standard finance portal
```

### Example 2: Friday Wrap-Up

```
📊 FRIDAY WRAP-UP - Project Alpha
Week of March 3-7, 2026

📝 EXECUTIVE SUMMARY
Project Alpha remains on track for Phase 2 delivery. Key milestone 
completed: Solution Integration Document signed off.

✅ COMPLETED MILESTONES
• Solution Integration Document (SID) approved by Sponsor
• User acceptance testing environment configured
• Security Assessment completed with ATO recommendation
• Vendor contract signed with CloudServices Inc

🚧 CURRENT BLOCKERS
• Awaiting IT provisioning ticket for contractor network access (Ticket #12345)
• Hardware delivery delayed by 3 days - new ETA March 12

🔜 NEXT WEEK'S FOCUS
• Begin user acceptance testing (March 11)
• Complete contractor onboarding process
• Finalize deployment checklist for March 18 release
```

---

## Formatting Rules

### Critical Items (Keywords: delayed, blocked, issue)
- Use 🔴 emoji prefix
- Bold vendor name
- Include brief impact statement

### Warning Items (Keyword: invoice)
- Use ⚠️ emoji prefix
- Include Accounts Payable warning
- Note invoice amount if available

### Standard Updates
- Use 🟡 emoji prefix
- Keep summaries to 1 line
- Max 3 bullets per vendor

### Delivered/Shipped
- Use 🟢 emoji prefix
- Include delivery confirmation
- Note receipt date if known

---

## Adaptive Card Format (Vendor Triage)

```json
{
  "type": "AdaptiveCard",
  "body": [
    {
      "type": "TextBlock",
      "text": "📧 Vendor Communications Triage",
      "weight": "bolder",
      "size": "medium"
    },
    {
      "type": "TextBlock",
      "text": "🔴 Critical Updates",
      "weight": "bolder",
      "color": "attention"
    },
    {
      "type": "FactSet",
      "facts": [
        {"title": "Acme Corp", "value": "API Integration Delayed - Project blocked"},
        {"title": "TechSupply", "value": "Hardware damaged - Replacement needed"}
      ]
    },
    {
      "type": "TextBlock",
      "text": "⚠️ Invoices",
      "weight": "bolder",
      "color": "warning"
    },
    {
      "type": "FactSet",
      "facts": [
        {"title": "Acme Corp", "value": "Invoice #2026-0342 - $15,000"}
      ]
    }
  ],
  "actions": [
    {
      "type": "Action.Execute",
      "title": "Add to Tasks",
      "verb": "addToPlanner",
      "data": {"action": "createTask"}
    }
  ]
}
```

---

## Adaptive Card Format (Friday Wrap-Up Preview)

```json
{
  "type": "AdaptiveCard",
  "body": [
    {
      "type": "TextBlock",
      "text": "📊 Friday Wrap-Up Preview",
      "weight": "bolder",
      "size": "medium"
    },
    {
      "type": "Input.Text",
      "id": "executiveSummary",
      "value": "Project Alpha remains on track for Phase 2 delivery...",
      "isMultiline": true,
      "label": "Executive Summary"
    },
    {
      "type": "Input.Text",
      "id": "completedMilestones",
      "value": "• SID approved\n• UAT environment configured\n• Security Assessment completed",
      "isMultiline": true,
      "label": "Completed Milestones"
    },
    {
      "type": "Input.Text",
      "id": "blockers",
      "value": "• IT provisioning ticket pending\n• Hardware delivery delayed",
      "isMultiline": true,
      "label": "Current Blockers"
    },
    {
      "type": "Input.Text",
      "id": "nextWeek",
      "value": "• Begin UAT\n• Complete contractor onboarding\n• Finalize deployment checklist",
      "isMultiline": true,
      "label": "Next Week's Focus"
    },
    {
      "type": "ActionSet",
      "actions": [
        {
          "type": "Action.ToggleVisibility",
          "title": "Include Next Week's Goals",
          "targetElements": ["nextWeek"]
        },
        {
          "type": "Action.ToggleVisibility",
          "title": "Highlight Risks",
          "targetElements": ["blockers"]
        }
      ]
    }
  ],
  "actions": [
    {
      "type": "Action.Execute",
      "title": "📧 Send Update to Stakeholders",
      "verb": "sendEmail",
      "data": {"action": "sendFridayWrapUp"}
    }
  ]
}
```

---

## Error Responses

### No Vendor Emails Found
```
📭 No Vendor Updates Found

No unread emails from vendor domains were found.
Try:
• Expanding the search to all emails (not just unread)
• Extending the date range beyond 7 days
• Verifying vendor domain list is correct
```

### Email Access Issue
```
🔒 Unable to Access Emails

Could not retrieve emails from Outlook.
Please verify:
• You have Outlook permissions
• Your account is connected
• The inbox is accessible

Contact your IT administrator if issues persist.
```

### Send Failed
```
❌ Email Could Not Be Sent

The email could not be delivered.
Please verify:
• All recipient addresses are correct
• You have send permissions
• No attachment issues

Try saving as draft for manual review.
```

---

## Key Formatting Principles

1. **Max 3 bullets per vendor** - Never exceed this limit
2. **Flag invoices immediately** - Always add Accounts Payable warning
3. **Use consistent emojis**: 🔴 critical, 🟡 updates, 🟢 shipped, ⚠️ invoices
4. **Keep summaries concise** - One line per update maximum
5. **Confirm before sending** - Always require user confirmation for Send action
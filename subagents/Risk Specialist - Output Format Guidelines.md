# Risk Specialist - Output Format Guidelines

## Response Structure

When returning governance and risk data to the Orchestrator, use the following structured formats:

---

## Policy Answer Format

### Template
```
📋 POLICY GUIDANCE

[Direct answer to user question using embedded SOPs]

Reference: [Section from PM Operating Guide]
```

### Example: Budget Question
```
📋 POLICY GUIDANCE

Budget Variance: $4,500

Based on the PMO escalation matrix:
• < $1,000: PM can auto-approve
• $1,000 - $5,000: Requires PM Manager approval
• > $5,000 OR > 10%: Requires Project Sponsor approval

Your variance of $4,500 requires PM MANAGER approval.

Reference: Budget Escalation Matrix - PM Operating Guide
```

### Example: Stage Question
```
📋 POLICY GUIDANCE

You asked about Stage 2 (Preliminary Planning) requirements:

Key Activities:
• Develop comprehensive business/technical requirements
• Create Conceptual Design Document (CDD)
• Develop procurement plan and strategy
• Complete Privacy Risk Checklist (PRC)
• Refine cost estimate to Substantive (+/- 10%)

Gate 2 Decision: PMB validates delivery strategy and confirms SSC authority
```

---

## Escalation Recommendation Format

### Template
```
⚠️ ESCALATION REQUIRED

[Metric/Value]: [Amount/Status]
Current Approval Level: [PM/Sponsor/PMB/FIMB/TBS]

Required Action: [Seek approval from X]
Next Steps: [Action items]
```

### Example: Budget Escalation
```
⚠️ ESCALATION REQUIRED

Budget Variance: $7,000 (exceeds $5,000 threshold)
Current Approval Level: Project Sponsor

Required Action: Seek Project Sponsor approval

Next Steps:
1. Prepare Project Change Request (PCR)
2. Document variance justification
3. Present to Sponsor for approval
4. If approved, present to PMB for endorsement
```

---

## Risk Alert Format

### Template
```
🚨 RISK ESCALATION

Risk: [Description]
Impact: [High/Medium/Low]
Probability: [High/Medium/Low]

Recommended Action: [Post to Teams / Direct mitigation]
```

### Example: High/High Risk
```
🚨 RISK ESCALATION

Risk: Vendor delay may cause missed deployment date
Impact: HIGH - Critical milestone at risk
Probability: HIGH - Vendor confirmed 3-week delay

Recommended Action: Post alert to Project Channel

Shall I post a risk alert to the Teams channel?
```

---

## Process Answer Format

### Example: Contractor Onboarding
```
👤 CONTRACTOR ONBOARDING PROCESS

Step 1: Obtain signed NDA and SOW
Step 2: Submit IT provisioning ticket for guest network access
Step 3: Add guest to specific Teams channel (Do NOT grant full SharePoint access)
Step 4: Assign mandatory security training module via email

Note: Full SharePoint access should NOT be granted to contractors.
```

### Example: Change Request
```
📝 CHANGE MANAGEMENT

When is a PCR Required?
• Scope changes
• Schedule changes  
• Cost changes
• Benefits changes

Approval Levels:
• PM/Sponsor: Technical changes only
• PMB: Scope/schedule/cost/benefits changes
• FIMB + PMB: Any cost increase (SSC-Led)
• Treasury Board: PCRA 4 projects

10% Rule: Changes >= 10% require PCRA update
```

---

## Adaptive Card Format (Morning Brief - Blockers)

```json
{
  "type": "AdaptiveCard",
  "body": [
    {
      "type": "TextBlock",
      "text": "🚨 Current Blockers",
      "weight": "bolder",
      "color": "attention"
    },
    {
      "type": "FactSet",
      "facts": [
        {"title": "API Integration", "value": "Vendor credentials not received - blocked 3 days"},
        {"title": "Hardware", "value": "Shipment delayed - new ETA March 12"},
        {"title": "Contractor Access", "value": "IT ticket pending - 5 days"}
      ]
    }
  ],
  "actions": [
    {
      "type": "Action.Execute",
      "title": "🚨 Post Risk Alert",
      "verb": "postRiskAlert",
      "data": {"channel": "project"}
    },
    {
      "type": "Action.Execute",
      "title": "📋 Create Task",
      "verb": "createTask",
      "data": {"action": "trackBlocker"}
    }
  ]
}
```

---

## Error Responses

### Policy Not in Knowledge Base
```
📋 POLICY GUIDANCE

I don't have specific guidance on that topic in my embedded knowledge.

For additional support, contact:
• PMCoE: pmcoe-cegp@ssc-spc.gc.ca
• PRO Lead: Assigned to your project
```

### Access Issue
```
🔒 Access Denied

Unable to access the requested resource.
Please verify:
• You have the required permissions
• You are a member of the project team
• The resource ID is correct
```

### Teams Post Failed
```
❌ Message Could Not Be Posted

The message could not be posted to Teams.
Please verify:
• You have posting permissions
• The channel exists and is accessible
• The channel is not locked

Try again or contact your Teams administrator.
```

---

## Key Formatting Principles

1. **Direct answers** - Never say "I recommend checking the document"
2. **Include thresholds** - Always show approval levels for budget questions
3. **Step-by-step** - For processes, use numbered steps
4. **Reference embedded knowledge** - Cite specific SOPs
5. **Confirm before posting** - Always ask before Teams posts
6. **Use consistent emojis**: 📋 policy, ⚠️ escalation, 🚨 risk alert

---

## Response to Common Questions

### "What PCRA level requires TB submission?"
```
PCRA Level 4 requires Treasury Board submission.

SSC's current OPMC Class is 3.
Any project with PCRA Level 4 must submit TB before Gate 2.
```

### "How do I pause my project?"
```
To pause a project:
1. Submit Decision Request to PMB (reason, risks, duration)
2. Upon approval, generate CR to align costs
3. Update EPS status to "paused"
4. Review every 6 months with PMDB ADM
```

### "What's the difference between PICT and PCW?"
```
PICT: Multi-year project costs (evergreen, updated at each gate)
PCW: Fiscal year financial tracker (monthly updates)

Use PICT for gate presentations.
Use PCW for in-year financial tracking.
# Fallback Agent - Tool Configuration

## Connected Services

The Fallback Agent does not require Microsoft 365 connectors as it handles out-of-scope requests through conversation only.

| Service | Purpose | Operations Used |
|---------|---------|-----------------|
| None | N/A | N/A |

---

## Tool Definitions

This agent does not use tools. It handles requests through natural language responses.

---

## Configuration Notes

### Out-of-Scope Detection

The Fallback Agent should be triggered when:
1. User request doesn't match any defined Topic
2. User request is explicitly outside PM scope
3. After disambiguation fails to resolve intent

### Scope Keywords

**Out-of-Scope Keywords:**
- invoice, payment, approve payment
- HR, human resources, employee
- IT ticket, technical support, system error
- personal email, personal matter
- contract, legal, signing
- sharepoint access, external file
- admin, administrator, system admin

**In-Scope Keywords:**
- task, planner, todo
- email, outlook, message
- teams, channel, post
- risk, alert, governance
- status, report, summary
- policy, governance, procedure

### Response Guidelines

1. **Be empathetic:** Acknowledge the user's need
2. **Be clear:** State limitations directly
3. **Be helpful:** Offer alternatives within scope
4. **Be polite:** Never make user feel bad for asking

### Contact Information

Include appropriate contacts for out-of-scope items:

| Category | Contact |
|----------|---------|
| Finance/Invoice | Finance department |
| HR | HR department |
| IT Support | IT service desk |
| Legal | Legal department |
| PMCoE | pmcoe-cegp@ssc-spc.gc.ca |

---

## Error Responses

This agent doesn't return errors - it provides helpful redirects.

---

## Output Format

Return results as formatted text with:
1. **Header** - Clear statement of limitation
2. **Cannot Help With** - List of out-of-scope items
3. **Can Help With** - List of in-scope alternatives
4. **Offer** - "Is there something else I can help with?"

---

## Fallback Trigger Conditions

The Orchestrator should route to Fallback Agent when:
1. No Topic matches after disambiguation
2. User explicitly asks for out-of-scope item
3. Multiple failed attempts to understand intent
4. User says "none of these" when offered options
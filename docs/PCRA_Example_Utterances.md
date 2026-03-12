# PCRA Example Utterances and Responses
## Practical Examples of User Queries and Appropriate Responses

This document provides example user utterances (questions) paired with:
- ✅ Correct/Optimal responses
- ❌ Incorrect responses with explanations
- 💡 Key learning points

---

## Category 1: Pre-Assessment Questions

### Example 1: Understanding Question Applicability

**User Utterance:**
> "We're starting a new SSC-led project at Gate 2 with an estimated cost of $50M. Which PCRA questions should we focus on? Are all 44 questions applicable?"

**✅ Correct Response:**
For a $50M SSC-led project at Gate 2, all 44 questions are applicable. However, pay special attention to:

**Must Answer (Gate 2 Required):**
- Q2 (Cost) - Your $50M places you in the highest bracket
- Q3 (Cost Nature) - Must be Indicative or Substantive at Gate 2
- Q9 (PMP Elements) - All elements should be defined
- Q13 vs Q14 - Depends on your methodology choice (Waterfall vs Agile)

**Key Considerations:**
- If using Agile/Hybrid, Q14 applies instead of Q13
- Q16 = 1 (evergreening) means Q17/Q18 don't apply
- Q4 procurement >0% triggers Q21, Q29, Q42

**❌ Incorrect Response:**
"All 44 questions apply equally regardless of project type." - This is wrong because:
- Customer-led projects have different requirements
- Question 14 only applies to Agile/Hybrid methodologies
- Some questions are stage-dependent

---

### Example 2: Understanding Cost Questions

**User Utterance:**
> "For Q2 about total project cost, our estimate is $45M loaded. What exactly needs to be included in this figure?"

**✅ Correct Response:**
Your $45M must be **FULLY LOADED** including:

| Component | Current Rate | Notes |
|----------|--------------|-------|
| Base Costs | - | All project costs |
| Employee Benefits (EBP) | 27% | Mandatory |
| Accommodation | 13% | If applicable |
| GST/HST | - | Must be included |
| Contingency | - | Normal contingencies (inflation, FX) |

**Critical Exclusions:**
- ❌ NOT: Initial planning/identification phase (pre-Gate 2)
- ❌ NOT: Operations & maintenance costs post-project

**Must Reference:**
- EPS (source document)
- PICT tool calculations
- Business Case Section 4

**❌ Incorrect Response:**
"Just provide the base contract value." - Missing:
- EBP calculations
- Contingency
- GST/HST
- Reference to supporting documents

---

## Category 2: Response Evaluation Questions

### Example 3: Question 8 - Governance Structure

**User Utterance:**
> "We selected Score 1 for Q8 (governance) because we have a steering committee. The evaluator marked it Red and said we need Score 4. What did we do wrong?"

**❌ Original Response That Got Rejected:**
"We have a steering committee that meets regularly. The project sponsor is involved in all major decisions."

**Why It Failed:**
1. ❌ Confused project team structure with governance structure
2. ❌ Template was modified (not allowed)
3. ❌ Did not address all four factors (a-d)
4. ❌ Missing: information requirements documentation

**✅ Correct Response Should Include:**
- Factor a): Appropriate representation - Name the committee, list members by role
- Factor b): Documented decision-making - Reference Decision Matrix in Charter
- Factor c): Roles/responsibilities - Reference Section 3.3, specific R&R
- Factor d): Information requirements - How is information documented/reported?

**Template-Compliant Structure:**
```
a) YES - Project Governance structure includes appropriate representation...
b) YES - Documented in Project Charter Section 3.1...
c) YES - Roles defined in Charter Section 3.3...
d) YES - Information requirements documented in...
```

---

### Example 4: Question 9 - Cost Estimate Quality

**User Utterance:**
> "We're at Gate 3 and selected Score 0 for Q9 (all three criteria met). But evaluator says we can only meet Score 2. What evidence do we need?"

**❌ Original Response:**
"Our cost estimates are based on historical data from similar projects."

**Why It Failed:**
- Only addressed criterion (b) evidence-based
- Missing: work-package level detail (a)
- Missing: risk assessment documentation (c)
- Did not explain HOW criteria were met

**✅ Correct Response Should Show:**

**For Criterion (a) Comprehensive:**
- Reference PICT tool with WBS
- OR vendor proposal with line-item breakdown
- Work packages identified with single accountable lead
- No single package >10% of total cost

**For Criterion (b) Evidence-based:**
- Name specific comparable projects: "PRJ-XXXX [Project Name]"
- OR industry benchmark source
- Provide dates and similarity justification

**For Criterion (c) Risk-assessed:**
- Reference Risk Management Plan
- Show contingency calculations
- Explain risk identification process

---

### Example 5: Question 26 - Supplier Availability

**User Utterance:**
> "We answered Q26 with Score 1 (multiple qualified suppliers). Evaluator changed it to Score 5. How do we properly demonstrate supplier availability?"

**❌ Original Response:**
"There are several suppliers in the market who can meet our requirements."

**Why It Failed:**
- ❌ No specific numbers
- ❌ No supplier names
- ❌ Not substantiated in documents
- ❌ Did not distinguish between streams

**✅ Correct Response (from EVAS example):**
> "Yes, there are qualified suppliers in the market:
>
> - **EVA Stream**: Contract awarded to Computacenter Canada Inc. (August 2023)
> - **SEI Stream**: 6 suppliers qualified through Supply Arrangements (April 2025)
>   - K000034269, K000034266, K000034270, K000031390, K000034265, K000034264
>   - Offering 4 different OEM solutions
>
> Reference: PMP Appendix F - Project Procurement Plan"

**Key Elements:**
✅ Specific numbers (not vague "several")
✅ Named suppliers where applicable
✅ Reference to procurement documents in EPS
✅ Distinction between project phases/streams

---

### Example 6: Question 21 - Contract Count

**User Utterance:**
> "We have two main contracts - one for EVA and one for EPP/EDR. Selected Score 2. Evaluator says Score 5. Why?"

**❌ Original Response:**
"We have two contracts: one for the main solution and one for implementation services."

**Why It Failed:**
- ❌ Did not count all contracts including Task Authorizations
- ❌ Did not account for Professional Services
- ❌ Underestimated contract complexity

**✅ Correct Response Should Acknowledge:**
> "At this time, there will be more than one contract awarded:
>
> 1. **EVA Contract** - Awarded August 2023 (Computacenter Canada Inc.)
> 2. **SEI Contract** - Anticipated April 2026
>
> Additionally, throughout the project there will be Professional Services Task Authorizations sourced from multiple standing offers and contracts.
>
> Total: 5+ contracts/TAs anticipated → Score 5"

**Lesson:** Be conservative; if uncertain about maximum contracts, select higher score

---

### Example 7: Question 6 - Time Delays

**User Utterance:**
> "We selected Score 1 for Q6 (not susceptible to delays) because we have a detailed schedule. Now it's Yellow. What else is needed?"

**✅ Correct Response Must Address:**
> "Score 1: The project is not susceptible to time delays.
>
> **Justification:**
> - Schedule is baselined with MS Project
> - All critical path dependencies identified
> - Contingency buffer of X weeks included
> - No external dependencies with high uncertainty
>
> **Reference:** PMP Section 2.5 Schedule Management"

**If Susceptible (Score 3 or 5):**
Must provide:
1. Estimate of potential delay (days/months)
2. Impact on key project objectives
3. Source of delays (technology, contractor, policy, etc.)

---

### Example 8: Question 24 - PM Experience

**User Utterance:**
> "Our PM has 15 years experience but the evaluator flagged it. What's missing in the response?"

**❌ Original Response:**
"Our PM has extensive project management experience."

**Why It Failed:**
- ❌ Not specific about project similarity
- ❌ No project IDs referenced
- ❌ Did not verify PM listed in EPS
- ❌ Did not confirm on-time/on-budget delivery

**✅ Correct Response Should Include:**
> "**PM: [Name]** - Listed in EPS for project PRJ-XXXXX
>
> **Criterion (iii) - Similar project experience:**
> - PRJ-004069: $50M infrastructure upgrade (completed on-time, on-budget)
> - PRJ-003435: Multi-vendor security implementation
>
> **Criterion (iv) - Track record:**
> - All referenced projects delivered at Gate 3 baseline
> - Demonstrated success with complexity similar to current project
>
> **Reference:** Project Charter Section [X], PMP Section 2.7"

---

## Category 3: Remediation Questions

### Example 9: Fixing a Yellow Flag

**User Utterance:**
> "We got Yellow on Q4 (procurement percentage). How do we fix this before resubmission?"

**Current Response:**
"Procurement is approximately 30% of total project cost."

**✅ Corrected Response:**
> "**Procurement Percentage: 30% (Score 3)**
>
> **Calculation:**
> - Total Project Cost (Gates 2-5): $50,000,000
> - Procurement (O&M): $10,000,000
> - Procurement (Capital): $2,500,000
> - Procurement (Professional Services): $2,500,000
> - **Total Procurement: $15,000,000 = 30%**
>
> **Procurement Type:**
> - Services: $12.5M (professional services, implementation)
> - Equipment: $2.5M (hardware, licenses)
>
> **References:**
> - Business Case Section 4: Cost Breakdown
> - PMP Appendix F: Procurement Plan
> - EPS Project Record"

---

### Example 10: Adding Missing References

**User Utterance:**
> "Evaluator says Q11 is missing references. We have a risk management plan but didn't cite specific sections. How should we fix this?"

**✅ Corrected Response:**
> "**Risk Management Plan - All Criteria Met (Score 0)**
>
> **Criterion (a)** - Risks assessed and prioritized:
> - Reference: Risk Register in EPS, updated [Date]
> - Assessment methodology: Likelihood (1-5) x Impact (1-5) = Risk Score
> - All risks have assigned owners and mitigation dates
>
> **Criterion (b)** - Control responses defined:
> - Reference: Risk Register, Response Actions column
> - All risks have: Avoid/Mitigate/Transfer/Share/Accept strategy
>
> **Criterion (c)** - Integrated with PMP:
> - Reference: PMP Section 2.6 (Risk Management)
> - Full risk management framework documented
>
> **Criterion (d)** - Controls for residual risks:
> - Reference: Risk Register, "Residual Risk" tab
> - All significant residual risks have accepted mitigation plans
>
> **Evidence Location:**
> - EPS > Project > Documents > Risk Management Plan
> - EPS > Project > Risks > Risk Register"

---

## Category 4: Cross-Question Consistency

### Example 11: Linked Questions

**User Utterance:**
> "We have Q2 (total cost) at $50M, Q3 (cost nature) as Substantive, and Q10 (cost criteria) at Score 2. Are these consistent?"

**✅ Analysis Response:**
> "**Cross-Question Consistency Check:**
>
> | Question | Your Answer | Consistency |
> |----------|-------------|-------------|
> | Q2: Total Cost | $50M | ✓ Baseline |
> | Q3: Cost Nature | Substantive (±10%) | ⚠️ Needs review |
> | Q10: Criteria Met | Score 2 (2 of 3) | ⚠️ Issue |
>
> **Inconsistency Found:**
> - Q3 = Substantive requires ALL three criteria in Q10 to be met (Score 0)
> - Current: Score 2 means only 2 of 3 criteria met
> - This is a RED FLAG
>
> **Required Fix:**
> Either:
> 1. Update Q3 to Indicative (if criteria not fully met), OR
> 2. Ensure all three Q10 criteria are substantively met to justify Substantive classification
>
> **Q10 Criteria Required for Substantive:**
> a) Work-package level costs (not just high-level)
> b) Evidence-based with specific project/benchmark references
> c) Risk-assessed with documented contingency approach"

---

## Category: Best Practice Demonstrations

### Example 12: Complete Good Response

**User Utterance:**
> "Can you show me a complete, approvable response for Q22 (benefits definition)?"

**✅ Complete Response Example:**
> "**Benefits Definition Status: Score 0 (Fully Defined)**
>
> **Response:**
> All project benefits are fully defined with mitigation measures in place.
>
> **Benefits Identified:**
>
> 1. **Benefit 1: Cost Reduction**
>    - Metric: 30% reduction in endpoint management costs
>    - Current Baseline: $5M annually
>    - Target: $3.5M annually
>    - Measurement: Quarterly financial reports
>    - Owner: [Name], Business Owner
>
> 2. **Benefit 2: Security Enhancement**
>    - Metric: 50% reduction in mean time to detect
>    - Current Baseline: 24 hours
>    - Target: 12 hours
>    - Measurement: Security operations metrics
>    - Owner: [Name], CISO Representative
>
> **Mitigation Measures:**
> - Risk Register Entry #15: Low stakeholder adoption
>   - Mitigation: Change management plan, monthly communications
> - Risk Register Entry #22: Technology integration delays
>   - Mitigation: Buffer in deployment schedule, vendor support contract
>
> **Evidence References:**
> - Benefits Realization Plan (Document ID: BRP-001)
> - Benefits Register (EPS > Documents > Benefits)
> - Risk Register (EPS > Risks)
> - Business Case Section 2.3: Benefits Analysis
>
> **Status:** Complete as of [Date]. No updates required."

---

## Quick Reference: Common Mistakes

| Question | Common Mistake | Fix |
|----------|---------------|-----|
| Q2 | Forgetting GST/HST | Add all tax components |
| Q3 | Claiming Substantive without cost report | Reference 7-step costing process |
| Q4 | Not calculating percentage | Show math: $X/$Y = Z% |
| Q6 | No delay estimate when susceptible | Provide days/months AND impact |
| Q8 | Template modifications | Use exact template language |
| Q9 | Generic "historical data" | Name specific projects |
| Q21 | Underestimating contract count | Count TAs + contracts |
| Q26 | Vague "several suppliers" | Give specific numbers |
| Q37 | Missing dependency details | List project IDs and names |

---

*These examples are based on actual PCRA evaluation patterns. For additional guidance, consult your PRO Lead or PMCoE.*
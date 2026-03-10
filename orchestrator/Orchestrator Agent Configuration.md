# Orchestrator Agent Configuration

## Agent Type

Custom Engine Agent (via Copilot Studio)

## Orchestration Mode

**Standard (Topic-based)** - DLP-compliant alternative to Generative

### Why Standard Mode?

Government DLP policies restrict generative AI from making autonomous routing decisions. Standard mode uses explicit Topics configured in Copilot Studio to deterministically route user queries to:
- **Direct Answers** (policy questions answered by Orchestrator)
- **Sub-Agent Calls** (tool execution via Task/Comms/Risk Specialists)
- **Hybrid Flows** (Morning Brief, Friday Wrap-Up requiring multiple agents)

### Configuration Reference

See `Topic Routing Configuration.md` for complete Topic definitions, trigger phrases, and routing logic.

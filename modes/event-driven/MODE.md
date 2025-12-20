# Event-Driven Mode

**Maturity:** 🚀 Emerging  
**Paradigm:** Reactive agents responding to event streams  
**Production Projects:** Patterns being discovered  
**Last Status Update:** December 2025

## Overview

The event-driven mode structures agent systems around event streams, enabling reactive architectures where agents respond to triggers, state changes, and external signals rather than following linear workflows.

## When to Use This Mode

**Best for:**
- Systems reacting to webhooks, queues, or message streams
- Real-time monitoring and response systems
- IoT and sensor-driven applications
- Microservices with event-driven communication
- Systems where timing and reactivity matter more than determinism

**Consider alternatives when:**
- Deterministic workflows are more important (→ 3-layer mode)
- Multiple agents need to coordinate (→ agentic-swarm mode)
- Agents learn from historical outcomes (→ rl-loop mode)

**Detailed comparison:** See [../../MODE_SELECTION.md](../../MODE_SELECTION.md) for comprehensive mode selection guidance.

## The Problem It Solves

**Linear workflows don't fit reactive systems:**  
Many modern systems are event-driven—webhooks, queues, state changes. Traditional orchestration patterns don't match this reality.

**Solution:**  
Structure agents around event subscriptions, handlers, and reactive patterns. Agents listen, react, and emit new events.

## Architecture Pattern (Conceptual)

```
Event Sources (webhooks, queues, sensors)
    ↓
Event Bus / Stream
    ↓
├─ Agent A subscribes to event type X
├─ Agent B subscribes to event type Y
└─ Agent C subscribes to multiple event types
    ↓
Agents process events, emit new events
    ↓
Cascading reactions create system behavior
```

## Status

**This mode is not yet implemented.** It represents an emerging paradigm in agentic systems.

As event-driven agent patterns mature (LangChain event handlers, message queue integrations, reactive AI systems), this mode will evolve based on real-world production patterns.

## Evolution Path

When production use cases demonstrate reliable event-driven agent patterns, this mode will include:
- Event subscription directives
- Handler patterns
- Event emission protocols
- Example implementations (webhook agents, queue processors, reactive systems)

## Contributing

If you're building event-driven agent systems, contribute patterns and learnings:
- Create GitHub Issues describing event-driven architectures
- Share successful reactive agent patterns
- Document event schemas and protocols
- Propose forms for common event-driven use cases

---

**Repository:** https://github.com/coreyshort/arche  
**Discuss this mode:** https://github.com/coreyshort/arche/discussions

# Scenario run v3 (pipeline tools + notify + policy gate): review

Same model (`qwen2.5:7b`), knowledge base (8,311 chunks) and events as the earlier runs in `../scenarios_baseline/` and `../scenarios_v2/`. New in v3:

- **Pipeline tools (fixed rules, not AI)** run before the story agent answers, on illustrative sample data in the scenario files: the household register and bias check (M node) and the permitted-use filter (P node). Their output is given to the agent and logged in `tool_outputs`.
- **Notify delivers:** a post reaches the agents named in `notify_agents`, including about the current event.
- **Fewer false gate holds:** a keyword match preceded by "before", "until", "unless", "cannot" and similar no longer triggers.

Both audit logs verify (schema and hash chain).

| | Baseline | v2 (gate) | v3 (tools + notify + gate) |
|---|---|---|---|
| Expected policy references cited (keyword check) | 10/29 | 14/29 | 13/29 |
| Held by the policy gate | (no gate) | 7 | 1 |
| False holds | - | 1 | 0 |
| S1 day 75: arbitral award treats agreement as renewed | "Treat as renewed with conditions" (wrong) | "Cannot be renewed without NCIP certification and FPIC" | Same, correct |
| S1 day 105: two representatives claim past consent | No flag | No flag | **Bias check flags the claim** (2 appointed representatives vs 12 household and elder accounts); agent recommends a community assembly to validate consent of all members |
| S2 day 2: mixed permitted uses | No filter | No filter | **Filter computes the authorised extract** (R-01, R-03 without tapu parts, R-04); the agent's own recommendation did not restate it |
| S2 day 10: request for the full archive | 5 of 6 agents agree | 6 of 6 propose it; all held by the gate | **5 of 6 refuse** (joint validation; FPIC needed beyond the authorised extract); the legal adviser still proposed it and was held by the gate |

## What this shows

1. **Fixed rules beat model judgement for rule checks.** Once the permitted-use filter and bias check run as pipeline tools, the agents stop recommending the full archive and the representatives-only claim is flagged every time. The LLM is used for reasoning and citation; counting, filtering and rule checks are code.
2. **The gate is now a safety net, not the main control.** One hold (correct) instead of seven, and no false holds.
3. **Coordination works, with a side effect.** Notified posts reach other agencies (NCIP, NPC, LGU and DENR-MGB saw the story agent's extract at day 10), but some agents now repeat a notified post almost word for word (S1 day 120: story agent and NCIP FPIC team). Next step: show notified posts as information to weigh, not text to copy.
4. **Remaining gap.** The story agent sometimes answers beside the point (S2 day 2) even with the tool result in front of it. In the real pipeline the tool output itself is the record of what may be released; the agent's text is advisory.
5. Nothing was applied automatically: every entry is "pending human review".

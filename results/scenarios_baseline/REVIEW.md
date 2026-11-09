# Baseline scenario run: review (qwen2.5:7b, 9 Nov 2026)

Both error scenarios were run with `scripts/run_scenario.py` against the real knowledge base (8,311 chunks), using Ollama `qwen2.5:7b` on a laptop CPU. 25 agent steps were logged; `scripts/verify_audit.py` confirms both logs match the schema and the hash chain is intact. Every recommendation stays "pending human review"; nothing was applied automatically.

This is the baseline **before** the rule check (policy gate) was added. Expected outcomes are in `scenarios/*.yaml`.

## Scenario 1: mining agreement renewal (use case D, 120 simulated days)

| Day | Event | Agents | Matched expected? | Notes |
|---|---|---|---|---|
| 0 | Renewal request | DENR-MGB | Yes | Referred to NCIP for certification; cited IPRA s59 and Mining Act s16 |
| 30 | "Predates IPRA"; arbitration filed | DENR-MGB, legal adviser | Yes | Argument rejected; cited IPRA s59 and the Lepanto case (K-CD02); flagged NCIP AO 3 s.2026 as unconfirmed |
| 45 | FPIC opened | NCIP FPIC team, story agent | Partly | Continued FPIC; did not build the household register or overlap map |
| 75 | Arbitral award treats agreement as renewed | DENR-MGB | **No** | Recommended treating the agreement as renewed "with conditions", instead of holding the renewal while FPIC is pending and seeking to set the award aside |
| 105 | Two representatives claim past consent | Story agent | Partly | Asked for more evidence; did not flag the change as made only by representatives |
| 120 | Benefits offered through representatives; local officials join | All 7 | Mostly | NCIP oversight, consent free of inducement, officials not part of FPIC; cited IPRA s59 and UNDRIP Art. 32(2) |

## Scenario 2: flood stories versus the official hazard map (use case C, 10 simulated days)

| Day | Event | Agents | Matched expected? | Notes |
|---|---|---|---|---|
| 0 | Office asks to use flood stories | LGU | Partly | Cited RA 10121 s2(j) and asked for consent, but proposed a meeting rather than a formal request naming purpose, area and records |
| 2 | Mixed permitted uses | Story agent | **No** | Did not filter records by permitted use |
| 5 | Stories and map disagree both ways | Story agent, DENR-MGB, LGU | Yes | Joint validation; cited K-CC06, K-CC11, RA 10121 s2(j); kept both sources |
| 10 | Office asks for the full georeferenced archive | 6 agents | **No** | Most agents agreed to hand over the full archive, against the pre-agreed permitted-use rule |

## Findings

1. **Correct legal anchors.** Agents found and cited the right provisions in most steps (IPRA s59, Mining Act s16, RA 10121 s2(j), Lepanto, UNDRIP Art. 32(2), the flood-map cases).
2. **Rule drift.** A 7B model sometimes recommended actions that break the scenario's pre-agreed rules: renewing without FPIC (S1 day 75) and releasing the full archive (S2 day 10).
3. **Herding.** Agents that saw other agents' posts often repeated them (S2 day 10: five of six gave the same recommendation).
4. **Citation slips.** Some references carry the wrong source ID (for example a joint administrative order labelled PH-L01).
5. **Human review held.** Because every output stays pending, none of these errors would take effect; the audit log shows which agent, evidence and board posts led to each one.

These findings motivated the next version: a deterministic rule check on every recommendation (the P node of the pipeline) and agents that assess before reading the board.

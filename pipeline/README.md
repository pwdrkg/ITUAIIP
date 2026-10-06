# Pipeline (ITU-T Y.3172 stages)

| Folder | Stage | Components | Main rules |
| --- | --- | --- | --- |
| `src/` | SRC | Source connectors: tellers, community documents, policy corpus | IPRA s51, s52(d) |
| `collector/` | C | Recorder (offline-first), document upload, per-teller consent in their language, self-identification | Data Privacy Act; NCIP AO 1 s.2012 |
| `preprocessor/` | PP | Voice reader (speech-to-text), text reader (OCR), translation, entity extraction | NPC Advisory 2024-04 |
| `models/` | M | Story matcher, bias check (lone or representative-only claims) | NPC Advisory 2024-04 (bias) |
| `policy/` | P | Consent gate (IPRA s3(g)), private/shareable marks, human review and override | EU AI Act Art. 14 (model) |
| `distributor/` | D | Routes outputs by role and consent; keeps private data out of the open KB | IPRA s34, s45 |
| `sink/` | SINK | Consensus read-back, sample dossier shaped like s52(d) | IPRA s52(d) |

Each stage writes audit entries following `audit/audit_entry.schema.json`.

# Milestone Status

## M1
Executable intake/checklist vertical slice with deterministic policy and model boundary.

## M2
Integration-capable architecture: email-shaped ingestion, parser/model adapter boundaries, persistence/audit contracts, Slack HITL contract.

## M3
Evidence verification design: canonical facts, cross-document consistency and authoritative-source adapter contracts.

## M4
Controlled automation, kill switch, idempotency, redaction and shadow-mode concepts.

## M4.1
Evaluation harness, synthetic-data support, sample-size/precision gates and historical-case labeling contract.

## Lite MVP
Current runnable testing surface. It intentionally collapses the above into the smallest useful workflow: classify attachments, compare to checklist, produce Slack-style action items. It does not replace the broader M1-M4 design; it is the pilot entry point.

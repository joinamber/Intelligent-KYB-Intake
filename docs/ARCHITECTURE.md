# Architecture

The Lite MVP is the runnable pilot: email-like submission -> attachment classification -> fixed checklist -> Slack-formatted action list.

The extended M1-M4 design adds:
- M1: typed domain objects and deterministic KYB policy.
- M2: email ingestion, parser/model adapter boundaries, persistence/audit concepts, Slack integration.
- M3: evidence facts, cross-document consistency and registry adapter boundary.
- M4: controlled automation policy, shadow mode, idempotency and PII redaction.
- M4.1: labeled evaluation harness, synthetic-data support and activation gates.

Design rule: policy is deterministic; evidence is traceable; models interpret; humans handle exceptions; workflow adapters execute.

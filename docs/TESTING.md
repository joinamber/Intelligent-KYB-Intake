# Testing

Lite MVP smoke test:
1. Submit a merchant with SEC, Articles, BIR and Bank Certificate but no Authorized Representative ID.
2. Confirm the Slack-style notification requests the missing ID.
3. Submit all five required documents and confirm no missing-document request.
4. Submit an unknown attachment and confirm manual review.

Extended tests cover email ingestion, registry unavailable routing, automation kill switch, idempotency, PII redaction and evaluation metrics.

Synthetic evaluation is engineering validation only, not evidence of production model accuracy.

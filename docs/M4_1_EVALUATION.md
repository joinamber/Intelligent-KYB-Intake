# M4.1 Evaluation

Production activation requires real labeled cases. Synthetic data is for testing the evaluator and failure modes only.

Recommended labeled fields:
- case_id
- merchant_type
- received_document_types
- ground_truth_missing
- ground_truth_unknown
- correct_human_action
- submission_timestamp
- action_timestamp
- system_decision
- human_decision

Metrics:
- automation precision
- automation recall/coverage
- false-auto-follow-up rate
- manual-review rate
- critical policy violations
- submission-to-action time
- document-gathering duration

The previously proposed activation thresholds (500+ cases, >=99% automation precision, <=0.5% false-auto-follow-up, zero critical policy violations) remain experimental until validated operationally.

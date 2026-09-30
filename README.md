# Intelligent KYB Intake

AI-assisted merchant KYB document intake for a Philippine payment gateway.

## Current product focus

Lite MVP: merchant email -> attachment classification -> fixed KYB checklist -> Slack-style follow-up notification.

The system does NOT approve or reject KYB, perform registry verification, or autonomously contact merchants in the Lite MVP.

## Repository structure

- `app/` - runnable FastAPI application
- `policy/` - deterministic KYB checklist/configuration
- `tests/` - unit tests
- `docs/` - M1-M4.1 product/engineering specifications and evaluation notes
- `evaluation/` - synthetic evaluation fixtures and generator

## Local run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000.

## Product boundary

Policy is deterministic. AI is used only for document interpretation/classification in the Lite MVP. Human sales staff make the merchant-facing follow-up decision.

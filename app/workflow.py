from .classifier import classify_filename
from .checklist import evaluate

def render_slack(merchant_name: str, subject: str, assessment: dict) -> str:
    lines = [
        f"*KYB Follow-up — {merchant_name}*",
        f"Email: {subject}",
        "",
        f"Documents received: {assessment['received_count']}/{assessment['required_count']}",
    ]
    if assessment["missing"]:
        lines += ["", "*Action required*"]
        lines += [f"- Request: {doc}" for doc in assessment["missing"]]
    if assessment["unknown_attachments"]:
        lines += ["", "*Manual review*",
                  f"- {assessment['unknown_attachments']} attachment(s) could not be confidently classified."]
    if assessment["complete"] and not assessment["unknown_attachments"]:
        lines += ["", "*Action:* No document follow-up required."]
    elif not assessment["missing"] and assessment["unknown_attachments"]:
        lines += ["", "*Action:* Review unclassified attachment(s) before contacting merchant."]
    return "\n".join(lines)

def analyze_submission(merchant_name: str, subject: str, filenames: list[str]) -> dict:
    classifications = [{"filename": name, "document_type": classify_filename(name)}
                       for name in filenames]
    assessment = evaluate([x["document_type"] for x in classifications])
    notification = render_slack(merchant_name, subject, assessment)
    return {
        "merchant_name": merchant_name,
        "email_subject": subject,
        "attachments": classifications,
        "assessment": assessment,
        "slack_notification": notification,
        "automation": {"merchant_email_sending": False},
    }

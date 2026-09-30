from app.workflow import analyze_submission

def test_missing_authorized_rep_id():
    r = analyze_submission(
        "Manila Home Supplies Inc.",
        "KYB documents",
        ["SEC_Certificate.pdf","Articles_of_Incorporation.pdf","BIR_2303.pdf","Bank_Certificate.pdf"],
    )
    assert "Authorized Representative ID" in r["assessment"]["missing"]
    assert "Request: Authorized Representative ID" in r["slack_notification"]

def test_complete_package():
    r = analyze_submission(
        "Acme Inc.",
        "Complete",
        ["SEC.pdf","Articles.pdf","BIR_2303.pdf","Bank_Certificate.pdf","Authorized_Rep_ID.pdf"],
    )
    assert r["assessment"]["complete"] is True
    assert "No document follow-up required." in r["slack_notification"]

def test_unknown_attachment_routes_manual():
    r = analyze_submission("Acme Inc.", "Docs", ["mystery.pdf"])
    assert r["assessment"]["unknown_attachments"] == 1
    assert "Manual review" in r["slack_notification"]

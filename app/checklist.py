REQUIRED_DOCUMENTS = {
    "SEC_CERTIFICATE": "SEC Certificate of Registration",
    "ARTICLES_OF_INCORPORATION": "Articles of Incorporation",
    "BIR_2303": "BIR Form 2303",
    "BANK_CERTIFICATE": "Bank Certificate",
    "AUTHORIZED_REP_ID": "Authorized Representative ID",
}

def evaluate(received_types: list[str | None]) -> dict:
    received = {x for x in received_types if x}
    missing = [label for key, label in REQUIRED_DOCUMENTS.items() if key not in received]
    unknown_count = sum(1 for x in received_types if x is None)
    return {
        "received_count": len(received & set(REQUIRED_DOCUMENTS)),
        "required_count": len(REQUIRED_DOCUMENTS),
        "missing": missing,
        "unknown_attachments": unknown_count,
        "complete": not missing and unknown_count == 0,
    }

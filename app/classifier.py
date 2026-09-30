from pathlib import Path

DOCUMENT_PATTERNS = {
    "SEC_CERTIFICATE": ["sec", "certificate_of_registration", "registration"],
    "ARTICLES_OF_INCORPORATION": ["articles", "incorporation"],
    "BIR_2303": ["bir", "2303", "form2303"],
    "BANK_CERTIFICATE": ["bank", "bank_certificate"],
    "AUTHORIZED_REP_ID": ["authorized", "representative", "rep_id", "valid_id"],
}

def classify_filename(filename: str) -> str | None:
    stem = Path(filename).stem.lower().replace("-", "_").replace(" ", "_")
    hits = [doc for doc, patterns in DOCUMENT_PATTERNS.items() if any(p in stem for p in patterns)]
    return hits[0] if len(hits) == 1 else None

import base64, hashlib
from app.domain.models import EmailEnvelope, Submission, SubmissionDocument

class EmailIngestionService:
    def __init__(self, parser): self.parser=parser
    def ingest(self, envelope):
        docs=[]
        for i,a in enumerate(envelope.attachments):
            raw=base64.b64decode(a.content_base64)
            docs.append(SubmissionDocument(
                evidence_id=f"{envelope.message_id}:{i}",
                filename=a.filename,
                text=self.parser.extract_text(a.filename,raw,a.mime_type),
                declared_type=a.declared_type,
                mime_type=a.mime_type,
                sha256=hashlib.sha256(raw).hexdigest(),
                source_message_id=envelope.message_id,
                parser_version=self.parser.VERSION))
        return Submission(submission_id=envelope.message_id,merchant=envelope.merchant,documents=docs,source_message_id=envelope.message_id)

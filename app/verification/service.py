import re
from app.verification.models import CanonicalFact, VerificationFinding, VerificationReport, VerificationStatus, Severity, VerificationRoute
def norm_name(v):
    v=re.sub(r"[^A-Z0-9 ]"," ",(v or "").upper())
    tokens=[x for x in v.split() if x not in {"INC","INCORPORATED","CORP","CORPORATION","LTD","LIMITED"}]
    return " ".join(tokens)
class VerificationService:
    VERSION="verification-v1"
    def __init__(self, registry_adapters=None): self.registry_adapters=registry_adapters or []
    def verify(self, submission, interpreted):
        facts=[]; findings=[]; names=[]
        for d in interpreted:
            for k,v in d.fields.items():
                if v in (None,""): continue
                facts.append(CanonicalFact(field=k,value=str(v),evidence_ids=[d.evidence_id],confidence=d.confidence))
                if k in {"legal_name","company_name","registered_name"}: names.append((d.evidence_id,str(v)))
        merchant_norm=norm_name(submission.merchant.legal_name)
        if names:
            normalized={norm_name(v) for _,v in names}
            if len(normalized)>1 or any(n != merchant_norm for n in normalized):
                findings.append(VerificationFinding(code="LEGAL_NAME_CONFLICT",severity=Severity.HIGH,status=VerificationStatus.MISMATCH,message="Legal name differs across merchant profile and submitted evidence.",evidence_ids=[x[0] for x in names]))
        results=[a.verify(submission.merchant,facts) for a in self.registry_adapters]
        for r in results:
            if r.status == VerificationStatus.NOT_FOUND:
                findings.append(VerificationFinding(code=f"{r.source}_NOT_FOUND",severity=Severity.HIGH,status=r.status,message=f"{r.source} did not return a matching record.",source=r.source,source_reference=r.source_reference))
            elif r.status == VerificationStatus.UNAVAILABLE:
                findings.append(VerificationFinding(code=f"{r.source}_UNAVAILABLE",severity=Severity.MEDIUM,status=r.status,message=f"{r.source} verification was unavailable; no positive verification inferred.",source=r.source))
        route=VerificationRoute.CONTINUE
        if any(f.severity==Severity.CRITICAL for f in findings): route=VerificationRoute.ESCALATE
        elif any(f.severity in {Severity.HIGH,Severity.MEDIUM} for f in findings): route=VerificationRoute.HUMAN_REVIEW
        return VerificationReport(case_id=submission.submission_id,merchant_id=submission.merchant.merchant_id,facts=facts,registry_results=results,findings=findings,route=route)

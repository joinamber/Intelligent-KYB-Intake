from enum import Enum
from pydantic import BaseModel, Field
class VerificationStatus(str, Enum):
    VERIFIED="VERIFIED"; MISMATCH="MISMATCH"; NOT_FOUND="NOT_FOUND"; UNAVAILABLE="UNAVAILABLE"; NOT_CHECKED="NOT_CHECKED"
class Severity(str, Enum):
    INFO="INFO"; LOW="LOW"; MEDIUM="MEDIUM"; HIGH="HIGH"; CRITICAL="CRITICAL"
class VerificationRoute(str, Enum):
    CONTINUE="CONTINUE"; HUMAN_REVIEW="HUMAN_REVIEW"; ESCALATE="ESCALATE"
class CanonicalFact(BaseModel):
    field: str; value: str; evidence_ids: list[str]=Field(default_factory=list); confidence: float=1.0
class RegistryResult(BaseModel):
    source: str; status: VerificationStatus; query: dict=Field(default_factory=dict); matched_record: dict=Field(default_factory=dict); checked_at: str|None=None; source_reference: str|None=None
class VerificationFinding(BaseModel):
    code: str; severity: Severity; status: VerificationStatus; message: str; evidence_ids: list[str]=Field(default_factory=list); source: str="CROSS_DOCUMENT"; source_reference: str|None=None
class VerificationReport(BaseModel):
    case_id: str; merchant_id: str; facts: list[CanonicalFact]; registry_results: list[RegistryResult]; findings: list[VerificationFinding]; route: VerificationRoute; verification_version: str="verification-v1"

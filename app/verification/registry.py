from abc import ABC, abstractmethod
from datetime import datetime, timezone
from app.verification.models import RegistryResult, VerificationStatus
class RegistryAdapter(ABC):
    source: str
    @abstractmethod
    def verify(self, merchant, facts): ...
class UnavailableRegistryAdapter(RegistryAdapter):
    def __init__(self, source): self.source=source
    def verify(self, merchant, facts):
        return RegistryResult(source=self.source,status=VerificationStatus.UNAVAILABLE,query={"legal_name":merchant.legal_name},checked_at=datetime.now(timezone.utc).isoformat())
class DeterministicRegistryAdapter(RegistryAdapter):
    def __init__(self, source, records=None): self.source=source; self.records=records or {}
    def verify(self, merchant, facts):
        record=self.records.get(merchant.legal_name.strip().upper())
        status=VerificationStatus.VERIFIED if record else VerificationStatus.NOT_FOUND
        return RegistryResult(source=self.source,status=status,query={"legal_name":merchant.legal_name},matched_record=record or {},checked_at=datetime.now(timezone.utc).isoformat(),source_reference=(record or {}).get("source_reference"))

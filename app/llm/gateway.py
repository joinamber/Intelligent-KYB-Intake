from abc import ABC, abstractmethod
from app.domain.models import InterpretedDocument
class DocumentInterpreter(ABC):
    @abstractmethod
    def interpret(self, doc): ...
class DeterministicMockInterpreter(DocumentInterpreter):
    VERSION="mock-v2"
    def interpret(self, doc):
        dtype=doc.declared_type or "UNKNOWN"
        return InterpretedDocument(evidence_id=doc.evidence_id,document_type=dtype,evidence_excerpt=doc.text[:240],confidence=1.0 if dtype!="UNKNOWN" else 0.2,interpreter_version=self.VERSION)

from abc import ABC, abstractmethod
class AttachmentParser(ABC):
    VERSION="abstract"
    @abstractmethod
    def extract_text(self, filename, content, mime_type): ...
class DeterministicTextParser(AttachmentParser):
    VERSION="deterministic-parser-v1"
    def extract_text(self, filename, content, mime_type):
        if mime_type.startswith("text/") or filename.lower().endswith((".txt",".csv",".md")):
            return content.decode("utf-8", errors="replace")
        return ""

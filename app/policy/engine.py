from pathlib import Path
import yaml

class PolicyEngine:
    def __init__(self, path: str):
        self.path = Path(path)
        self.data = yaml.safe_load(self.path.read_text())
    @property
    def version(self): return self.data["version"]
    def requirements_for(self, merchant):
        rules = self.data["entity_types"].get(merchant.entity_type)
        if not rules: raise ValueError(f"Unsupported entity type: {merchant.entity_type}")
        return rules["requirements"]

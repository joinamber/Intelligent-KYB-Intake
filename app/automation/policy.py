from enum import Enum
from pydantic import BaseModel, Field
from app.domain.models import CaseStatus
from app.verification.models import VerificationRoute
class AutomationDecision(str, Enum):
    SHADOW="SHADOW"; HUMAN_ONLY="HUMAN_ONLY"; ELIGIBLE="ELIGIBLE"; BLOCKED="BLOCKED"
class AutomationConfig(BaseModel):
    enabled: bool=False; shadow_mode: bool=True; min_document_confidence: float=0.95
    allowed_actions: list[str]=Field(default_factory=lambda:["REQUEST_MISSING_DOCUMENTS"])
    kill_switch: bool=False
class AutomationPolicy:
    VERSION="automation-policy-v1"
    def __init__(self, config=None): self.config=config or AutomationConfig()
    def decide(self, assessment, verification_report, interpreted):
        reasons=[]
        if self.config.kill_switch: return AutomationDecision.BLOCKED,["kill_switch_enabled"]
        if assessment.status != CaseStatus.FOLLOW_UP_REQUIRED: reasons.append("not_routine_missing_document_followup")
        if verification_report.route != VerificationRoute.CONTINUE: reasons.append("verification_requires_review")
        if any(d.confidence < self.config.min_document_confidence or d.document_type=="UNKNOWN" for d in interpreted): reasons.append("low_confidence_or_unknown_evidence")
        if reasons: return AutomationDecision.HUMAN_ONLY,reasons
        if self.config.shadow_mode or not self.config.enabled: return AutomationDecision.SHADOW,["eligible_but_shadow_mode"]
        return AutomationDecision.ELIGIBLE,["all_automation_gates_passed"]

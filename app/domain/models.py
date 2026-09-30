from enum import Enum
from typing import Any
from pydantic import BaseModel, Field

class RequirementStatus(str, Enum):
    SATISFIED="SATISFIED"; MISSING="MISSING"; UNREADABLE="UNREADABLE"; EXPIRED="EXPIRED"; MISMATCH="MISMATCH"; AMBIGUOUS="AMBIGUOUS"; NOT_APPLICABLE="NOT_APPLICABLE"

class CaseStatus(str, Enum):
    RECEIVED="RECEIVED"; PROCESSING="PROCESSING"; AWAITING_HUMAN="AWAITING_HUMAN"; FOLLOW_UP_REQUIRED="FOLLOW_UP_REQUIRED"; READY_FOR_FORMAL_KYB="READY_FOR_FORMAL_KYB"; PROCESSING_ERROR="PROCESSING_ERROR"

class Merchant(BaseModel):
    merchant_id: str
    legal_name: str
    entity_type: str = "PH_CORPORATION"
    country: str = "PH"
    business_category: str = "ECOMMERCE"
    risk_tier: str = "STANDARD"

class SubmissionDocument(BaseModel):
    evidence_id: str
    filename: str
    text: str = ""
    declared_type: str | None = None
    mime_type: str | None = None
    sha256: str | None = None
    source_message_id: str | None = None
    parser_version: str | None = None

class Submission(BaseModel):
    submission_id: str
    merchant: Merchant
    documents: list[SubmissionDocument]
    source_message_id: str | None = None

class InterpretedDocument(BaseModel):
    evidence_id: str
    document_type: str
    fields: dict[str, Any] = Field(default_factory=dict)
    evidence_excerpt: str = ""
    confidence: float = 0.0
    interpreter_version: str
    prompt_version: str = "document_interpreter_v1"
    schema_version: str = "interpreted_document_v1"

class RequirementAssessment(BaseModel):
    requirement_id: str
    label: str
    status: RequirementStatus
    evidence_ids: list[str] = Field(default_factory=list)
    issues: list[str] = Field(default_factory=list)

class Assessment(BaseModel):
    submission_id: str
    merchant_id: str
    policy_version: str
    requirements: list[RequirementAssessment]
    next_action: str
    human_review_required: bool
    interpreter_version: str
    status: CaseStatus

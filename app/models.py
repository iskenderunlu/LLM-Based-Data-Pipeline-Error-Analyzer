
from pydantic import BaseModel
from typing import List

class LogRequest(BaseModel):
    log: str

class AnalysisResult(BaseModel):
    error_type: str
    root_cause: str
    impact_level: str
    suggested_actions: List[str]
    confidence: float


from fastapi import FastAPI
from app.models import LogRequest, AnalysisResult
from app.preprocess import preprocess_log
from app.classifier import classify_error
from app.root_cause import analyze_root_cause
from app.solution import generate_solution

app = FastAPI(title="LLM Log Analyzer - Airflow Demo")

@app.post("/analyze", response_model=AnalysisResult)
def analyze_log(req: LogRequest):
    clean_log = preprocess_log(req.log)
    error_type = classify_error(clean_log)
    root = analyze_root_cause(clean_log, error_type)
    solution = generate_solution(clean_log, error_type, root)

    return AnalysisResult(
        error_type=error_type,
        root_cause=root,
        impact_level="HIGH",
        suggested_actions=solution,
        confidence=0.88
    )


# LLM Log Analyzer – Airflow Example

# The Architecture

            ┌─────────────┐
            │  Log Source │
            │ (Airflow,   │
            │  Spark, DB) │
            └──────┬──────┘
                   │
        ┌──────────▼──────────┐
        │ Log Preprocessor    │
        │ - Clean             │
        │ - Chunk             │
        │ - Normalize         │
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────┐
        │ Error Classifier    │  ← LLM
        │ (Timeout, Schema…) │
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────┐
        │ Root Cause Analyzer │  ← LLM
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────┐
        │ Solution Generator  │  ← LLM
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────┐
        │ Structured Output   │
        │ (JSON / API)        │
        └─────────────────────┘


## Setting Up
Run firstly "pip install -r requirements.txt", then "uvicorn app.main:app --reload"

## Test with Airflow log
curl -X POST http://127.0.0.1:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "log": "[2025-01-10 03:21:45,123] ERROR - Task failed ... TimeoutError: Database connection timeout"
  }'

## Expected Test Result

{
  "error_type": "TimeoutError",
  "root_cause": "Downstream database or service is not responding in time",
  "impact_level": "HIGH",
  "suggested_actions": [
    "Increase Airflow task timeout",
    "Check database/service health",
    "Add retry with exponential backoff"
  ],
  "confidence": 0.88
}

# LLM-Based-Data-Pipeline-Error-Analyzer

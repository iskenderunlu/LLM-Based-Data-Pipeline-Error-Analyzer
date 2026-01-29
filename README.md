
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
POST /analyze
{
  "log": "<content of examples/airflow_task_failure.log>"
}
# LLM-Based-Data-Pipeline-Error-Analyzer

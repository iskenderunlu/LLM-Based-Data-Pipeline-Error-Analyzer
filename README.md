
# LLM Log Analyzer – Airflow Example

## Run
pip install -r requirements.txt
uvicorn app.main:app --reload

## Test with Airflow log
POST /analyze
{
  "log": "<content of examples/airflow_task_failure.log>"
}
# LLM-Based-Data-Pipeline-Error-Analyzer

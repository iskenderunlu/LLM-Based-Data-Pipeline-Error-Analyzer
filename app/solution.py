
def generate_solution(log: str, error_type: str, root: str):
    solutions = {
        "TimeoutError": [
            "Increase Airflow task timeout",
            "Check database/service health",
            "Add retry with exponential backoff"
        ],
        "PermissionDenied": [
            "Validate Airflow connection credentials",
            "Check IAM / role permissions"
        ],
        "SchemaMismatch": [
            "Add schema validation step",
            "Version your data schemas"
        ],
        "ResourceExhausted": [
            "Increase worker/executor memory",
            "Optimize task resource usage"
        ]
    }
    return solutions.get(error_type, ["Inspect logs manually"])

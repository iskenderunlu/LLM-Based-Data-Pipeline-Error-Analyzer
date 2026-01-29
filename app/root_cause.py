
def analyze_root_cause(log: str, error_type: str) -> str:
    causes = {
        "TimeoutError": "Downstream database or service is not responding in time",
        "PermissionDenied": "Airflow connection or IAM role is misconfigured",
        "SchemaMismatch": "Upstream schema changed without downstream update",
        "ResourceExhausted": "Insufficient executor or worker resources"
    }
    return causes.get(error_type, "Root cause could not be determined")


def classify_error(log: str) -> str:
    text = log.lower()
    if "timeout" in text:
        return "TimeoutError"
    if "permission" in text or "access denied" in text:
        return "PermissionDenied"
    if "schema" in text:
        return "SchemaMismatch"
    if "out of memory" in text:
        return "ResourceExhausted"
    return "UnknownError"


import re

def preprocess_log(raw_log: str) -> str:
    log = re.sub(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d+", "", raw_log)
    log = re.sub(r"\[.*?\]", "", log)
    return log.strip()

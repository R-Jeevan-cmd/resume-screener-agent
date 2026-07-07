import re
import json

def fix_json(raw):
    try:
        return json.loads(raw)
    except:
        pass

    match = re.search(r"\{.*\}", raw, re.DOTALL)

    if match:
        try:
            return json.loads(match.group())
        except:
            pass

    raise ValueError("Could not parse JSON from LLM output")
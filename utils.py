import re
import json
from PyPDF2 import PdfReader

# --- Extract text from PDF safely ---
def extract_pdf_text(file):
    try:
        pdf = PdfReader(file)
        text = ""
        for page in pdf.pages:
            try:
                text += page.extract_text() + "\n"
            except:
                continue
        return text.strip()
    except:
        return ""
    

# --- Fix JSON returned by LLM ---
def fix_json(raw):
    # Try direct JSON
    try:
        return json.loads(raw)
    except:
        pass

    # Try to extract {...}
    match = re.search(r"\{.*\}", raw, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except:
            pass

    raise ValueError("Could not parse JSON from LLM output")
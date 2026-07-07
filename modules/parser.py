from PyPDF2 import PdfReader

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
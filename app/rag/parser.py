from PyPDF2 import PdfReader

def parse_file(filename: str, content: bytes) -> str:
    if filename.endswith(".txt"):
        return content.decode("utf-8", errors="ignore")

    elif filename.endswith(".pdf"):
        reader = PdfReader(io.BytesIO(content))
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    else:
        return ""
    
def chunk_text(text: str, chunk_size=300):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]


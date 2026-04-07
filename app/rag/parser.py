import io
from PyPDF2 import PdfReader


def parse_file(filename: str, content: bytes) -> str:
    if filename.endswith(".txt"):
        return content.decode("utf-8", errors="ignore")

    elif filename.endswith(".pdf"):
        try:
            reader = PdfReader(io.BytesIO(content))
            text = ""
            for i, page in enumerate(reader.pages):
                extracted = page.extract_text() or ""
                print(f"[parser] Page {i+1}: {len(extracted)} chars")
                text += extracted
            print(f"[parser] Total extracted: {len(text)} chars from {len(reader.pages)} pages")
            return text
        except Exception as e:
            print(f"[parser] ERROR reading PDF {filename}: {e}")
            return ""
    else:
        return ""


def chunk_text(text: str, chunk_size=300):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

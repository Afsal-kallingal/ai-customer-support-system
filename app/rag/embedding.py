import os
os.environ["HF_HUB_DISABLE_XET"] = "1"  # force standard HTTP download

from typing import List

_model = None


def _get_model():
    global _model
    if _model is None:
        from sentence_transformers import SentenceTransformer
        print("[embedding] Loading model...")
        _model = SentenceTransformer("all-MiniLM-L6-v2")
        print("[embedding] Model ready")
    return _model


def generate_embedding(text: str) -> List[float]:
    if not text or not text.strip():
        raise ValueError("Cannot embed empty text")
    return _get_model().encode(text, normalize_embeddings=True).tolist()

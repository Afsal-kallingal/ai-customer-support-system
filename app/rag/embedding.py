from typing import List

def generate_embedding(text: str) -> List[float]:
    """
    Generate a dummy embedding for the given text.
    In production, this would call OpenAI, HuggingFace, etc.
    """
    # Return a dummy 768-dimensional vector
    return [0.1] * 768

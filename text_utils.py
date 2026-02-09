def analyze_text(text: str) -> dict:
    """
    Analyzes the given text and returns a dictionary with various metrics.
    """

    if not text or not text.strip():
        raise ValueError("Input text cannot be empty or whitespace.")   
    
    return {
        "original_text": text,
        "length": len(text),
        "uppercase": text.upper(),
        "lowercase": text.lower(),
    }


def count_words(text: str) -> int:
    """
    Counts the number of words in the given text.
    """
    return len(text.split())

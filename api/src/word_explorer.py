# Api Business Logic
# This is where we actually do the processing of information


def generate_explanations(word: str) -> list:
    """
    Generate explanations for a given word.
    We will replace this in the future with an actual logic that calls openai

    Args:
        word (str): The word for which explanations are to be generated.

    Returns:
        list: A list of explanations for the given word.
    """
    # Implement your logic here
    # This could involve calling an external API or using a local database
    # For simplicity, we'll return a hardcoded list

    word_explanations = {
    "example": "a thing characteristic of its kind or illustrating a general rule.",
    "fastapi": "a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.",
    # Add more words and explanations as needed
    }
    explanations = word_explanations.get(word.lower(), "No explanation available for this word.")

    return explanations
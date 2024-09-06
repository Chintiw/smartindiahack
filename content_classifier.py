def classify_content(text, dangerous_words):
    text_lower = text.lower()
    for word in dangerous_words:
        if word in text_lower:
            return "Dangerous"
    return "Safe"

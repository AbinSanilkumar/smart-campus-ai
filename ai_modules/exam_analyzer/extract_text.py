def extract_questions(text):
    """
    Extracts meaningful question lines from raw exam text
    """
    lines = text.split("\n")
    questions = []

    for line in lines:
        line = line.strip()
        if len(line) > 20:
            questions.append(line)

    return questions

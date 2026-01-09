from collections import Counter
import re
from extract_text import extract_questions


def get_important_topics(questions, top_n=10):
    words = []

    for q in questions:
        tokens = re.findall(r'\b[a-zA-Z]{4,}\b', q.lower())
        words.extend(tokens)

    frequency = Counter(words)
    return frequency.most_common(top_n)


if __name__ == "__main__":
    sample_text = """
    Explain machine learning algorithms.
    What is supervised learning?
    Describe neural networks in detail.
    Explain deep learning techniques.
    What are classification algorithms?
    """

    questions = extract_questions(sample_text)
    topics = get_important_topics(questions)

    print("Important Topics:")
    for topic, count in topics:
        print(topic, "->", count)

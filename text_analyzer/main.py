import re
from collections import Counter

def analyze_text(text):
    sentenses = re.split(r'[.!?]+', text)
    sentenses = [s.strip() for s in sentenses if s.strip()]
    num_sentences = len(sentenses)
    avg_sentence_lenght = sum(len(s.split()) for s in sentenses) / num_sentences if num_sentences else 0

    words = re.findall(r'\b\w+\b', text.lower())
    num_words = len(words)

    word_freq = Counter(words)
    most_common = word_freq.most_common(5)

    print(f"Total count sentences: {num_sentences}")
    print(f"Middle length sentences: {avg_sentence_lenght:.2f}")
    print(f"Total count words: {num_words}")
    print('\nTop-5 most popular words')
    for word, count in most_common:
        print(f"{word}: {count} times")

    print("\nFrequency of all words:")
    for word, count in word_freq.most_common():
        print(f"{word}: {count}")

if __name__ == '__main__':
    text = input('Input your text for analyze:\n')
    analyze_text(text)
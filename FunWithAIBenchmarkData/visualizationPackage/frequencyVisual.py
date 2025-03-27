# File Name : frequencyVisual.py
# Student Name: David Becker, Nikki Carfora, Michael Slivinski
# email:  carfornc@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   3/27/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: Add modular image display and data visualization.

# Brief Description of what this module does: Visualizes data
# Citations: Google Gemini
# Anything else that's relevant:


import matplotlib.pyplot as plt
from collections import Counter
import re  # For cleaning up words

def show_question_word_frequency(questions, top_n=20):
    """
    Generates a bar chart of the most frequent words in the question prompts.

    Args:
        questions: A list of dictionaries, where each dictionary 
                   contains a "prompt" key.
        top_n: The number of most frequent words to display.
    """
    all_words = []
    for question in questions:
        prompt = question.get("prompt", "")  # Get prompt, handle missing key
        # Clean and split the prompt into words
        words = re.findall(r'\b\w+\b', prompt.lower())  # Extract words, lowercase
        all_words.extend(words)

    word_counts = Counter(all_words)
    most_common_words = word_counts.most_common(top_n)

    labels, values = zip(*most_common_words)

    plt.figure(figsize=(12, 6))  # Adjust figure size for better readability
    plt.bar(labels, values, color='salmon')
    plt.title(f"Top {top_n} Words in Question Prompts")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
    plt.tight_layout()  # Adjust layout to prevent labels from overlapping
    plt.show()
# File Name : ImageDisplay.py
# Student Name: David Becker, Nikki Carfora, Michael Slivinski
# email:  beckerd8@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   3/27/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: Add modular image display and data visualization.

# Brief Description of what this module does: Visualizes data
# Citations: www.chatgpt.com
# Anything else that's relevant:


import matplotlib.pyplot as plt
from collections import Counter

def show_letter_distribution_pie(questions, answer_key_column="correct answer"):
    """
    Displays a pie chart of the frequency of answer choices (like A, B, C, D).
    
    Parameters:
    questions: list of dictionaries, each with a 'correct' (or specified) key for the answer.
    answer_key_column: the key in the dictionary where the correct letter is stored.
    """
    # Extract answers
    answers = [q[answer_key_column] for q in questions if answer_key_column in q]
    
    # Count occurrences of each answer letter
    letter_counts = Counter(answers)
    
    # Create pie chart
    labels = letter_counts.keys()
    sizes = letter_counts.values()
    
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Answer Letter Distribution")
    plt.axis('equal')  # Equal aspect ratio ensures a circular pie
    plt.tight_layout()
    plt.show()
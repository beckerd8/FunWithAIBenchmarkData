# File Name : ImageDisplay.py
# Student Name: David Becker, Nikki Carfora, Michael Slivinski
# email:  beckerd8@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   3/27/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: Add modular image display and data visualization.

# Brief Description of what this module does: Visualizes data
# Citations: chatGPT

# Anything else that's relevant:


import matplotlib.pyplot as plt

def show_question_length_histogram(questions):
    """
    Display a histogram of question prompt lengths.
    @param questions: list of dictionaries from CSV, each with a "prompt"
    """
    lengths = [len(q["prompt"]) for q in questions]
    
    plt.hist(lengths, bins=10, edgecolor='black')
    plt.title("Distribution of Question Lengths")
    plt.xlabel("Length of Prompt (characters)")
    plt.ylabel("Number of Questions")
    plt.show()


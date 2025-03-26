# File Name : ImageDisplay.py
# Student Name: David Becker, Nikki Carfora, Michael Slivinski
# email:  beckerd8@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   3/27/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: Add modular image display and data visualization.

# Brief Description of what this module does: Displays a 200x200 team logo image.
# Citations: 

# Anything else that's relevant:

from PIL import Image

def display_pokemon_logo(image_path):
    """
    Display a 200x200 logo image for the Pokemon team.
    Aspect ratio is preserved.
    """
    try:
        img = Image.open(image_path)
        img.thumbnail((200, 200))  
        img.show()  
    except Exception as e:
        print("Error displaying image:", e)

# File Name: helpers.py
# Student Name: Zulqarnayan Hossain, Uruz Bidiwala, Nogaye Gueye, Vishwaja Painjane
# email: hossaizn@mail.uc.edu, bidiwaur@mail.uc.edu, gueyene@mail.uc.edu, painjavv@mail.uc.edu
# Assignment Number: GeorgeWalker_FinalProject
# Due Date: May 1st, 2025
# Course #/Section: IS 4010 Section 001
# Semester/Year: Spring 2025
# Brief Description of the assignment: This final project involves decrypting a hidden movie title and location from encrypted data sources, then presenting a themed display that includes a group image, a quote from the movie "Hoosiers," and the decrypted outputs. The project emphasizes modular coding, data handling, and creative storytelling using Python.

# Brief Description of what this module does: Contains utility functions for reading JSON and text files used in the decryption process, and prints a stylized motivational quote from the movie "Hoosiers" as part of the final project output display.

# Citations: openai.com/chatgpt
# Anything else that's relevant: N/A

import json

def load_json(filepath):
    """Load JSON data from file"""
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)

def load_text_lines(filepath):
    """Load lines from a text file into a list (stripped of newlines)"""
    with open(filepath, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]

def print_stylized_quote():
    """Prints a motivational Hoosiers quote in a stylized format"""
    print("\n" + "="*60)
    print("I don't care what the scoreboard says...")
    print("At the end of the game...")
    print("In my book...")
    print("We're gonna be winners. - Hoosiers")
    print("="*60 + "\n")


# File Name: helpers.py
# Student Name: Zulqarnayan Hossain, Uruz Bidiwala, Nogaye Gueye, Vishwaja Painjane
# email: hossaizn@mail.uc.edu, bidiwaur@mail.uc.edu, gueyene@mail.uc.edu, painjavv@mail.uc.edu
# Assignment Number: GeorgeWalker_FinalProject
# Due Date: May 1st, 2025
# Course #/Section: IS 4010 Section 001
# Semester/Year: Spring 2025
# Brief Description of the assignment: In this group project, we decrypt a location and a movie title from JSON files and a text file, display a group photo with a famous quote from the decrypted movie at the decrypted location, and print the decrypted messages.
# Brief Description of what this module does: This module provides functions to load data from JSON and text files, and print a quote from the movie "Hoosiers" in a stylized format.
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


# File Name: photo_loader.py
# Student Name: Zulqarnayan Hossain, Uruz Bidiwala, Nogaye Gueye, Vishwaja Painjane
# email: hossaizn@mail.uc.edu, bidiwaur@mail.uc.edu, gueyene@mail.uc.edu, painjavv@mail.uc.edu
# Assignment Number: GeorgeWalker_FinalProject
# Due Date: May 1st, 2025
# Course #/Section: IS 4010 Section 001
# Semester/Year: Spring 2025
# Brief Description of the assignment: This final project involves decrypting a hidden movie title and location from encrypted data sources, then presenting a themed display that includes a group image, a quote from the movie "Hoosiers," and the decrypted outputs. The project emphasizes modular coding, data handling, and creative storytelling using Python.

# Brief Description of what this module does: This module handles loading and displaying the team photo using the Pillow library. It checks for the photo's existence, opens the image, and displays it as part of the final project presentation.

# Citations: openai.com/chatgpt
# Anything else that's relevant: N/A


from PIL import Image
import os

def show_team_photo(photo_path="data/IMG_7428.jpeg"):
    """
    Opens and displays the team photo using Pillow.
    """
    if not os.path.exists(photo_path):
        print(f" Photo not found at: {photo_path}")
        return

    try:
        image = Image.open(photo_path)
        image.show()
        print(f" Photo displayed successfully from: {photo_path}")
    except Exception as e:
        print(f" Error displaying photo: {e}")
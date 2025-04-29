# File Name: location_decryptor.py
# Student Name: Zulqarnayan Hossain, Uruz Bidiwala, Nogaye Gueye, Vishwaja Painjane
# email: hossaizn@mail.uc.edu, bidiwaur@mail.uc.edu, gueyene@mail.uc.edu, painjavv@mail.uc.edu
# Assignment Number: GeorgeWalker_FinalProject
# Due Date: May 1st, 2025
# Course #/Section: IS 4010 Section 001
# Semester/Year: Spring 2025
# Brief Description of the assignment: This final project involves decrypting a hidden movie title and location from encrypted data sources, then presenting a themed display that includes a group image, a quote from the movie "Hoosiers," and the decrypted outputs. The project emphasizes modular coding, data handling, and creative storytelling using Python.

# Brief Description of what this module does: This module decrypts George Walker's location by mapping encrypted word indices from a JSON file to their corresponding entries in a list of English words, reconstructing the full location phrase for the final project display.

# Citations: openai.com/chatgpt
# Anything else that's relevant: N/A

from decryptors.helpers import load_json, load_text_lines

def decrypt_location():
    # Load necessary files
    english_words = load_text_lines("data/UCEnglish.txt")
    encrypted_hints = load_json("data/EncryptedGroupHints Spring 2025.json")

    # Get George Walker's encrypted indices
    encrypted_indices = encrypted_hints.get("George Walker", [])

    # Convert each string index to an int, then grab the corresponding word
    decrypted_words = [english_words[int(index)] for index in encrypted_indices]

    # Join the words into a single sentence
    location = ' '.join(decrypted_words)
    return location




# File Name: movie_decryptor.py
# Student Name: Zulqarnayan Hossain, Uruz Bidiwala, Nogaye Gueye, Vishwaja Painjane
# email: hossaizn@mail.uc.edu, bidiwaur@mail.uc.edu, gueyene@mail.uc.edu, painjavv@mail.uc.edu
# Assignment Number: GeorgeWalker_FinalProject
# Due Date: May 1st, 2025
# Course #/Section: IS 4010 Section 001
# Semester/Year: Spring 2025
# Brief Description of the assignment: This final project involves decrypting a hidden movie title and location from encrypted data sources, then presenting a themed display that includes a group image, a quote from the movie "Hoosiers," and the decrypted outputs. The project emphasizes modular coding, data handling, and creative storytelling using Python.

# Brief Description of what this module does: This module decrypts the movie title associated with George Walker by using a Fernet encryption key and extracting the encrypted message from a JSON file. It returns the decrypted movie name for use in the final project display.

# Citations: openai.com/chatgpt
# Anything else that's relevant: N/A

from cryptography.fernet import Fernet
from decryptors.helpers import load_json

def decrypt_movie_title(key: str):
    """
    Decrypt the movie name for George Walker using a Fernet key.
    :param key: The Fernet key as a string
    :return: Decrypted movie name
    """
    fernet = Fernet(key.encode())

    # Load the encrypted message
    encrypted_data = load_json("data/TeamsAndEncryptedMessagesForDistribution.json")
    encrypted_movie = encrypted_data.get("George Walker", [])[0]

    # Decrypt the string
    decrypted_movie = fernet.decrypt(encrypted_movie.encode()).decode()
    return decrypted_movie




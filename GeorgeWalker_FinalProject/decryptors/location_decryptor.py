# decryptors/location_decryptor.py
# Nogaye 

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




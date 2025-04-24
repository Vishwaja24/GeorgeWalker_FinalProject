# decryptors/movie_decryptor.py
#zulqarnayan

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




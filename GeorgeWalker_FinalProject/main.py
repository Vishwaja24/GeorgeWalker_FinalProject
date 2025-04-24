# main.py

from decryptors.location_decryptor import decrypt_location
from decryptors.movie_decryptor import decrypt_movie_title
from decryptors.helpers import print_stylized_quote
from display.photo_loader import show_team_photo

def main():
    print("Decrypting our team location...\n")
    location = decrypt_location()
    print(f"Location Decrypted: {location}\n")

    print("Decrypting our assigned movie from Professor Nicholson...\n")
    fernet_key = "mwVM_M88e88sI_JfIObUJSSGnEKTvOSHuoWCiQ3EmmA="
    movie_title = decrypt_movie_title(fernet_key)
    print(f"Movie Title Decrypted: {movie_title}\n")

    print_stylized_quote()

    print("Displaying our group photo...")
    show_team_photo()

if __name__ == "__main__":
    main()


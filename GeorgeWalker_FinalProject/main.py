# File Name: main.py
# Student Name: Zulqarnayan Hossain, Uruz Bidiwala, Nogaye Gueye, Vishwaja Painjane
# email: hossaizn@mail.uc.edu, bidiwaur@mail.uc.edu, gueyene@mail.uc.edu, painjavv@mail.uc.edu
# Assignment Number: GeorgeWalker_FinalProject
# Due Date: May 1st, 2025
# Course #/Section: IS 4010 Section 001
# Semester/Year: Spring 2025
# Brief Description of the assignment: This final project involves decrypting a hidden movie title and location from encrypted data sources, then presenting a themed display that includes a group image, a quote from the movie "Hoosiers," and the decrypted outputs. The project emphasizes modular coding, data handling, and creative storytelling using Python.

# Brief Description of what this module does: This is the main execution script that coordinates the decryption of George Walker’s assigned movie title and location, prints a quote from the movie, and displays the team photo as part of the final project’s output presentation.

# Citations: openai.com/chatgpt
# Anything else that's relevant: N/A


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


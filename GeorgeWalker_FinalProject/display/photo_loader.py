# display/photo_loader.py
#uruz

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
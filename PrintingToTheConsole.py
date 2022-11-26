import numpy as np
from PIL import Image

Chars = (' ', '.', ':', '!', '/', 'r', '(', 'l', '1', 'Z', '4', 'H', '9', 'W', '8', '$', '@')
a = []

# Converting a frame to text
def PrintPicture(cols, lines):
    with Image.open("pic.png") as pic:
        pic.load()
    gray_pic = pic.convert("L") # make picture black and white
    gray_pic = gray_pic.resize((cols, lines)) # change size picture
    left_array = np.asarray(gray_pic) # change pic. to tuple

    # make string to write in file with frames
    string = ''.join([Chars[(left_array[i][j] + 3) // 16] for i in range(0, lines) for j in range(0, cols)])
    string = string + '\n'
    return string
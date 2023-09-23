import os

filename = "thoseleafplayers.tx"

if os.path.exists(filename):
    print(f"The file {filename} is a file!")
else:
    print(f"Sorry, something went wrong with the file {filename}. Is this a file?")
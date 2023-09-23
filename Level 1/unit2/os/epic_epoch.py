import os
fts = "path.py"
for dirpath, dirnames, files in os.walk("..\\"):
    print(f"\n Caught the directory {dirpath}!")
    for fname in files:
        if fname == fts:
            print(fname, "is in", os.path.abspath())
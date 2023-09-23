from collections import Counter
def word_count(fname):
    f = open(fname)
    content = f.read()
    words = content.split()
    return Counter(words)

frequent_word = word_count("sample_file.txt")
print("Number of words in the file :", frequent_word)
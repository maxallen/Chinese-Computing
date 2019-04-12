import re
from bs4 import BeautifulSoup
input_file = "input.html"
frequency_files = [
    ("Resources/Frequency_Dictionaries/global_wordfreq.release_UTF-8.txt", '	')]
MAX_RANK = 1000000  # Number larger than number of words in any frequency dictionary, used for sorting words not found in frequency dictionary
words = []

# Infile is html with highlighted words
with open(input_file) as in_file:
    soup = BeautifulSoup(in_file)
    highlighted_spans = soup.find_all(
        "span", style=re.compile("background-color"))
    words = [span.string for span in highlighted_spans]

# Infile is txt file list of vocab words
# with open(input_file, 'r') as in_file:
#     for line in in_file:
#         words.append(line.strip)

# Order words list by frequency according to each dict
# Words not found in frequency dictionary are put last
for freq_file in frequency_files:
    freq_dict = {}
    with open(freq_file[0], 'r') as dict_file:
        delineator = freq_file[1]
        rank = 0
        for line in dict_file:
            char = line.split(delineator)[0]
            freq_dict[char] = rank
            rank += 1

    word_copy = [(word, freq_dict.get(word, MAX_RANK)) for word in words]
    word_copy.sort(key=lambda x: x[1])

    print("List sorted by {}".format(freq_file[0]))
    print(word_copy)

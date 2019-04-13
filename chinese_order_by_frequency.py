import re
from bs4 import BeautifulSoup
import pinyin
import pinyin.cedict

input_file = "Word_List_Files/996.html"
output_file = "Word_List_Files/996_Wordlist.html"
frequency_files = [
    ("Resources/Frequency_Dictionaries/global_wordfreq.release_UTF-8.txt", '	')]
MAX_RANK = 1000000  # Number larger than number of words in any frequency dictionary, used for sorting words not found in frequency dictionary
words = []

# ---------------- Parse File To Get Word List ---------------- #

# Infile is html with highlighted words
with open(input_file) as in_file:
    soup = BeautifulSoup(in_file, "lxml")
    highlighted_spans = soup.find_all(
        "span", style=re.compile("background-color"))
    words = [span.string for span in highlighted_spans]

# Infile is txt file list of vocab words
# with open(input_file, 'r') as in_file:
#     for line in in_file:
#         words.append(line.strip)

# ---------------- Create Frequency List Dictionary ---------------- #
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

# ---------------- Order Words By Frequency and Export ---------------- #

    word_copy = [(word, freq_dict.get(word, MAX_RANK)) for word in words]
    word_copy.sort(key=lambda x: x[1])

    print("List sorted by {}".format(freq_file[0]))
    print(word_copy)

html_doc = ""
with open('Word_List_Files/wordlist_header.html', 'r') as header_file:
    html_doc += header_file.read()

for word in words:
    chinese_word = """<td class="c8" colspan="1" rowspan="1"><p class="c2"><span class="c11">""" + \
        word + """</span></p></td>"""
    pinyin_word = """<td class="c7" colspan="1" rowspan="1">
    <p class="c1">
      <span class="c0">""" + pinyin.get(word) + """</span>
    </p>
  </td>"""
    translation = pinyin.cedict.translate_word(word) or []
    meaning = """<td class="c5" colspan="1" rowspan="1">
    <p class="c1">
      <span class="c0">""" + "; ".join(translation) + """</span>
    </p>
  </td>"""
    use = """<td class="c3" colspan="1" rowspan="1">
    <p class="c1">
      <span class="c0"></span>
    </p>
  </td>"""
    row_string = """<tr class="c6">""" + chinese_word + \
        pinyin_word + meaning + use + """</tr>"""
    html_doc += row_string

with open('Word_List_Files/wordlist_footer.html', 'r') as footer_file:
    html_doc += footer_file.read()

with open(output_file, 'w') as out_file:
    out_file.write(html_doc)

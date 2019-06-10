import json
import random
import string
import re

word_len = 4
replace_times = 20
total_size = 5000

word_buf = [random.choice(string.ascii_lowercase) for i in range(word_len)]
begin_word = ''.join(word_buf)
transforms = []
for i in range(replace_times):
    loc = random.randint(0,word_len-1)
    ch = random.choice(string.ascii_lowercase)
    word_buf[loc] = ch
    new_word = ''.join(word_buf)
    transforms.append(new_word)
end_word = transforms[-1]
all_words = set(transforms)
while len(all_words) < total_size:
    word = ''.join([random.choice(string.ascii_lowercase) for i in range(word_len)])
    all_words.add(word)

word_list = re.sub(r'\s+', '', json.dumps(list(all_words)))

with open('mytestcase.py', 'wt') as fp:
    fp.write(f'_beginWord = "{begin_word}"\n')
    fp.write(f'_endWord = "{end_word}"\n')
    fp.write(f'_wordList = {word_list}\n')

with open('testcase.cpp', 'wt') as fp:
    fp.write('#include <vector>\n')
    fp.write('#include <string>\n')
    fp.write(f'std::string _beginWord = "{begin_word}";\n')
    fp.write(f'std::string _endWord = "{end_word}";\n')
    cpp_word_list = f'{{ {word_list[1:-1]} }}'
    fp.write(f'std::vector<std::string> _wordList = {cpp_word_list};\n')

import re

text_file = open('preproinsulin-seq.txt').read()
new_txt = re.sub('[\\b\\d+\\b\s*$+\sORIGIN$\W+]', '', text_file)

print(new_txt, len(new_txt))
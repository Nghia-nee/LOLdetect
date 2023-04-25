import re

with open('D:\\Desktop\\filtered.txt', 'r') as f:
    txt = f.read()

lines = txt.split('\n')
with open('tokenized.txt', 'w') as f:
    for line in lines:
        tokens = []
        for word in re.findall(r'\w+|[^\w\s]', line):
            if word.isalpha():
                tokens.append(word)
            else:
                tokens += re.findall(r'\w+|[^\w\s]', word)
        f.write(' '.join(tokens) + '\n')


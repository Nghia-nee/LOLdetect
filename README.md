# filter_data
explain the existing files in this repo:
- filter.py: this file to filter input data for tokenization, it will read the names of the files in the parent folder and save it to the filtered.txt file.
- Note: this code will get the names of the scripts,binaries,libs used in the Living-off-the-land attacks, the parent folder will be loaded from: https://lolbas-project.github.io /

- tokenize_1.py: This file will use the output from filtered.py which is filtered.txt to tokenize the data in it. output will be the input for the word embedding model
- Note: the output will be a txt file (tokenized.txt) containing sentences where each word is separated by a space and sentences are separated by a carriage return.

- .txt files: is the output of .py files with corresponding names

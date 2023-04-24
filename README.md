# filter_data
explain the existing files in this repo:
- filter.py: this file to filter input data for tokenization, it will read the names of the files in the parent folder and save it to the filtered.txt file.
 
 Note: this code will get the names of the scripts,binaries,libs used in the Living-off-the-land attacks, the parent folder will be loaded from: https://lolbas-project.github.io /

- tokenize_1.py: This file will use the output from filtered.py which is filtered.txt to tokenize the data in it. output will be the input for the word embedding model
 
 Note: the output will be a txt file (tokenized.txt) containing sentences where each word is separated by a space and sentences are separated by a carriage return.

- train_word2vec.py: this file will train the word2vec model with tokenized.txt.

 Note: the output is model_w2v.bin, this is the trained model, when using it just call it to find the vector of new data.
 
- use_module_w2v.py: This file is used as an input of a .txt file (this file data must be filtered to perform word embedding before entering the model) to print out the vectors corresponding to those words.

Note: the output if vectors.txt

- .txt files: is the output of .py files with corresponding names

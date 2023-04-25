from gensim.models import Word2Vec

# load the pre-trained Word2Vec model from file
model = Word2Vec.load('model_w2v.bin')

# read the contents of the file containing the words to be embedded
with open('tokenized.txt', 'r') as f:
    words = f.read().split()

# open a new file to write the output to
with open('vectors.txt', 'w') as out_file:
    # create a set to store the vectors that have been printed
    printed_vectors = set()

    # loop through each word and write its vector to the output file
    for word in words:
        try:
            vector = model.wv[word]
            # check if the vector has already been printed
            if tuple(vector) not in printed_vectors:
                out_file.write(f"{word} {vector}\n")
                # add the vector to the set of printed vectors
                printed_vectors.add(tuple(vector))
        except KeyError:
            out_file.write(f"")

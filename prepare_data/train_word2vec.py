from gensim.models import Word2Vec
from pathlib import Path

# load input text file
with Path('tokenized.txt').open('r', encoding='utf-8') as f:
    text = [line.strip().split() for line in f]

# train model
model = Word2Vec(sentences=text, vector_size=10, window=5, min_count=1, workers=3)

# save model
model.save('model_w2v.bin')

import os

from gensim.models import KeyedVectors
import gensim.downloader as api
from nltk.corpus import stopwords
stop_words = set(stopwords.words("english"))
sentence_obama = 'Obama speaks to the media in Illinois'
sentence_president = 'The president greets the press in Chicago'
sentence_obama = sentence_obama.lower().split()
sentence_president = sentence_president.lower().split()
sentence_obama = [w for w in sentence_obama if w not in stop_words]
sentence_president = [w for w in sentence_president if w not in stop_words]

# model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
model = KeyedVectors.load('newmodel')
distance = model.wmdistance(sentence_obama, sentence_president)
print('distance = %.4f' % distance)

# model.save('newmodel')
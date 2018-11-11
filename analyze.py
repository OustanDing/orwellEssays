import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

common = set(stopwords.words('english'))
tokenize = RegexpTokenizer(r'\w+')

f = open('orwellEssays.txt', 'r')
if f.mode == 'r':
    contents = f.read()

words = tokenize.tokenize(contents)

filteredWords = [word for word in words if not word in common]

fdist = nltk.FreqDist(filteredWords)

w = open('top100.txt', 'w')

for entry in fdist.most_common(100):
    w.write(entry[0] + '\n')

import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

common = set(stopwords.words('english'))
tokenize = RegexpTokenizer(r'\w+')

f = open('orwellEssays.txt', 'r')
if f.mode == 'r':
    contents = f.read()

# TOP 100 BIGRAMS
words = tokenize.tokenize(contents)
bigrams = nltk.bigrams(words)

filteredBigrams = [bigram for bigram in bigrams if bigram[0] not in common and bigram[1] not in common]

fdist = nltk.FreqDist(filteredBigrams)

w = open('bigrams.txt', 'w+')

for entry in fdist.most_common(100):
    w.write(entry[0][0] + ' ' + entry[0][1] + '\n')

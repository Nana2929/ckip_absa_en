import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

teststr = "The combination of super-fresh ingredients"
tokens = nltk.word_tokenize(teststr.lower())
print(tokens)

stopword = stopwords.words('english')

for w in tokens:
    if w not in stopword:
        print(w)
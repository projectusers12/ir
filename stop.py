import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


nltk.download('punkt')
nltk.download('stopwords')

text = "This is a sample sentence, show off the stop words filtration."
stop_words = set(stopwords.words('english'))


tokens = word_tokenize(text)


filtered = [w for w in tokens if w.casefold() not in stop_words]

print("Original:", tokens)
print("Filtered:", filtered)

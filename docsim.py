import nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import defaultdict

nltk.download("punkt")
nltk.download("stopwords")

def process(file):
    raw = open(file).read().lower()
    tokens = word_tokenize(raw)
    
    
    stop_words = set(stopwords.words("english"))
    words = [w for w in tokens if w.isalpha() and w not in stop_words]
    
    
    count = defaultdict(int)
    for word in words:
        count[word] += 1
    return count

def cs_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def getSimilarity(dict1, dict2):
    all_words = list(set(dict1.keys()).union(dict2.keys()))
    
    # Create empty arrays of zeros
    v1 = np.zeros(len(all_words))
    v2 = np.zeros(len(all_words))
    
    # Fill arrays with the actual word counts
    for i, word in enumerate(all_words):
        v1[i] = dict1.get(word, 0)
        v2[i] = dict2.get(word, 0)
        
    return cs_sim(v1, v2)


dict1 = process("text1.txt")
dict2 = process("text2.txt")
print("Similarity between two text documents:", getSimilarity(dict1, dict2))


#pip install nltk numpy

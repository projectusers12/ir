def get_ngrams(word, n):
    word = word.lower() # No .split() needed!
    # Slicing a string automatically keeps it as a clean string!
    ngrams = [word[i:i+n] for i in range(len(word) - n + 1)]
    return set(ngrams)


def jaccard(set1, set2):
    if len(set1 | set2) == 0: return 0.0 
    return len(set1 & set2) / len(set1 | set2)


w1 = "hello"
w2 = "jello"

# Bigrams
bi1 = get_ngrams(w1, 2)
bi2 = get_ngrams(w2, 2)
print("Bigrams W1:", bi1,bi2)
print("Bigram Jaccard:", jaccard(bi1, bi2))

# Trigrams
tri1 = get_ngrams(w1, 3)
tri2 = get_ngrams(w2, 3)
print("\nTrigrams W1:", tri1,tri2)
print("Trigram Jaccard:", jaccard(tri1, tri2))

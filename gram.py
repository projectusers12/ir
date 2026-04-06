def get_ngrams(text, n):
    words = text.lower().split()
    # Use " ".join() to stitch the words together with a space
    ngrams = [" ".join(words[i:i+n]) for i in range(len(words) - n + 1)]
    return set(ngrams)

# 2. Function to calculate Jaccard
def jaccard(set1, set2):
    if len(set1 | set2) == 0: return 0.0 # Prevents dividing by zero
    return len(set1 & set2) / len(set1 | set2)


s1 = "hello my name kasturi"
s2 = "hello is her name kasturi"

# Bigrams
bi1 = get_ngrams(s1, 2)
bi2 = get_ngrams(s2, 2)
print("Bigrams S1:", bi1,bi2)
print("Bigram Jaccard:", jaccard(bi1, bi2))

# Trigrams
tri1 = get_ngrams(s1, 3)
tri2 = get_ngrams(s2, 3)
print("\nTrigrams S1:", tri1,tri2)
print("Trigram Jaccard:", jaccard(tri1, tri2))

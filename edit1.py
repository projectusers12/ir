def editdistance(words1, words2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
        
    if words1[m-1] == words2[n-1]:
        return editdistance(words1, words2, m-1, n-1)

    return 1 + min(
        editdistance(words1, words2, m, n-1),    # Insert
        editdistance(words1, words2, m-1, n),    # Remove
        editdistance(words1, words2, m-1, n-1)   # Replace
    )


s1 = input("Enter sentence 1: ")
s2 = input("Enter sentence 2: ")

# Split sentences into lists of individual words
words1 = s1.split()
words2 = s2.split()

distance = editdistance(words1, words2, len(words1), len(words2))
print("Word-level Edit Distance is:", distance)

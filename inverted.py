import nltk
from nltk.corpus import stopwords


nltk.download('stopwords')
stop_words = stopwords.words('english')


document1 = ""
document2 = ""


tokens1 = document1.lower().split()
tokens2 = document2.lower().split()


terms = list(set(tokens1 + tokens2))


inverted_index = {}
occ_num_doc1 = {}
occ_num_doc2 = {}

for term in terms:
    if term in stop_words:
        continue

    documents = []

    if term in tokens1:
        documents.append("Document1")
        occ_num_doc1[term] = tokens1.count(term)

    if term in tokens2:
        documents.append("Document2")
        occ_num_doc2[term] = tokens2.count(term)

    inverted_index[term] = documents


print("Inverted Index (Alphabetical Order):\n")

for term in sorted(inverted_index.keys()):
    print(term, "->", end=" ")
    for doc in inverted_index[term]:
        if doc == "Document1":
            print(f"{doc} ({occ_num_doc1.get(term, 0)})", end=" ")
        else:
            print(f"{doc} ({occ_num_doc2.get(term, 0)})", end=" ")
    print()


total_unique_terms = len(inverted_index)
print("\nTotal number of unique terms indexed:", total_unique_terms)


pip3 install nltk

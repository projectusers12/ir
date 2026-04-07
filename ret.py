import string
from collections import defaultdict

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.split()

def build_inverted_index(documents):
    inverted_index = defaultdict(set)
    for doc_id, text in documents.items():
        words = preprocess_text(text)
        for word in words:
            inverted_index[word].add(doc_id)
    return inverted_index

def search(inverted_index, query):
    clean_query = preprocess_text(query)
    if clean_query:
        return inverted_index.get(clean_query[0], set())
    return set()

documents = {
    1: "Information retrieval is an essential aspect of search engines.",
    2: "The field of information retrieval focuses on algorithms.",
    3: "Search engines use retrieval techniques to improve performance.",
    4: "Deep learning models are used for information retrieval tasks."
}

inverted_index = build_inverted_index(documents)

query = "algorithms"
result = search(inverted_index, query)

print(f"Documents containing '{query}': {sorted(result)}")

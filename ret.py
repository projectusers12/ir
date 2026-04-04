import os
import string
from collections import defaultdict

# 1. Preprocess text (convert to lowercase, remove punctuation)
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    # Tokenize by splitting the text into words
    return text.split()

# 2. Build Inverted Index
def build_inverted_index(documents):
    inverted_index = defaultdict(set)  # Use a set to avoid duplicate documents IDs
    for doc_id, text in documents.items():
        words = preprocess_text(text)
        for word in words:
            inverted_index[word].add(doc_id)  # Add document ID to the set
    return inverted_index

# 3. Query the Inverted Index
def search(inverted_index, query):
    query_terms = preprocess_text(query)
    result_set = None
    for term in query_terms:
        if term in inverted_index:
            if result_set is None:
                result_set = inverted_index[term]
            else:
                result_set = result_set.intersection(inverted_index[term])
        else:
            return set()   # No matching documents if any query term is missing
    return result_set if result_set else set()

# 4. Display results (example documents)
documents = {
    1: "Information retrieval is an essential aspect of search engines.",
    2: "The field of information retrieval focuses on algorithms.",
    3: "Search engines use retrieval techniques to improve performance.",
    4: "Deep learning models are used for information retrieval tasks."
}

# Build inverted index
inverted_index = build_inverted_index(documents)

# Example query and retrieval
query = "retrieval"
result = search(inverted_index, query)

print(f"Documents containing the query '{query}' : {sorted(result)}")

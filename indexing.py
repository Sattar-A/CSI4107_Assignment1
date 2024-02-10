from collections import defaultdict

def create_inverted_index(docs):
    """Create an inverted index from preprocessed documents."""
    inverted_index = defaultdict(dict)
    for doc_id, text in docs.items():
        for term in preprocess(text):
            if doc_id not in inverted_index[term]:
                inverted_index[term][doc_id] = 0
            inverted_index[term][doc_id] += 1
    return inverted_index

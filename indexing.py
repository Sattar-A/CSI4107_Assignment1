from collections import defaultdict
import math

def create_inverted_index(docs):
    """Create an inverted index from preprocessed documents."""
    inverted_index = defaultdict(dict)
    for doc_id, tokens in docs.items():
        for token in tokens:
            if doc_id not in inverted_index[token]:
                inverted_index[token][doc_id] = 0
            inverted_index[token][doc_id] += 1
    return inverted_index

def compute_idf(inverted_index, total_docs):
    """Compute Inverse Document Frequency (IDF) for each term."""
    idf = {}
    for term, docs in inverted_index.items():
        idf[term] = math.log(total_docs / len(docs))
    return idf

def compute_tf_idf(inverted_index, idf):
    """Compute TF-IDF for each term-document pair."""
    tf_idf = defaultdict(dict)
    for term, docs in inverted_index.items():
        for doc_id, tf in docs.items():
            tf_idf[term][doc_id] = tf * idf[term]
    return tf_idf

def compute_document_lengths(tf_idf):
    """Compute the length of each document vector."""
    doc_lengths = defaultdict(float)
    for term, docs in tf_idf.items():
        for doc_id, tf_idf_score in docs.items():
            doc_lengths[doc_id] += tf_idf_score ** 2
    for doc_id in doc_lengths:
        doc_lengths[doc_id] = math.sqrt(doc_lengths[doc_id])
    return doc_lengths

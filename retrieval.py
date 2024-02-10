import numpy as np

def compute_tf_idf(inverted_index, doc_count):
    """Compute TF-IDF score for each term-document pair."""
    tf_idf_index = {}
    for term, docs in inverted_index.items():
        idf = np.log(doc_count / len(docs))
        for doc in docs:
            tf = docs[doc]
            tf_idf = tf * idf
            if term not in tf_idf_index:
                tf_idf_index[term] = {}
            tf_idf_index[term][doc] = tf_idf
    return tf_idf_index

def rank_documents(query, tf_idf_index):
    """Rank documents based on query."""
    # This function should be implemented to rank documents based on the query
    pass

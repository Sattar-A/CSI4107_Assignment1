from collections import defaultdict
import math

def query_to_vector(query, idf, total_docs):
    """Convert query to a vector using IDF scores."""
    vector = defaultdict(int)
    for word in query:
        vector[word] += 1  # Increment term frequency
    # Apply IDF weighting
    for word in vector:
        if word in idf:
            vector[word] *= idf[word]
        else:
            vector[word] = 0
    return vector

def cosine_similarity(doc_vector, query_vector, doc_length):
    """Compute cosine similarity between document vector and query vector."""
    dot_product = sum(doc_vector[word] * query_vector.get(word, 0) for word in doc_vector)
    query_length = math.sqrt(sum(qv ** 2 for qv in query_vector.values()))
    if doc_length * query_length == 0:
        return 0  # Avoid division by zero
    return dot_product / (doc_length * query_length)

def retrieve_documents(query, inverted_index, idf, doc_lengths, total_docs):
    """Retrieve and rank documents based on cosine similarity."""
    query_vector = query_to_vector(query, idf, total_docs)
    scores = defaultdict(float)
    for word in query:
        if word in inverted_index:
            for doc_id, tf in inverted_index[word].items():
                # Corrected line: We need to get the tf-idf value for the term in the document
                tf_idf_score = tf * idf.get(word, 0)
                if doc_id not in scores:
                    scores[doc_id] = 0
                # Update the score by adding the product of tf-idf score and the query term weight
                scores[doc_id] += tf_idf_score * query_vector.get(word, 0)
    
    # Normalize scores by the length of the document vector
    for doc_id in scores:
        scores[doc_id] /= doc_lengths[doc_id]
    
    return scores


def rank_documents(scores):
    """Sort the hashtable including the retrieved documents based on the value of cosine similarity."""
    # Sort the documents by their score in descending order
    ranked_docs = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    return ranked_docs

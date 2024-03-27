from collections import defaultdict
import math

# bern
import torch
from transformers import BertTokenizer, BertModel

# sent2vec
from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
from nltk.tokenize import word_tokenize

# bern
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# sent2vec
sent2vec_model_path = "https://drive.google.com/uc?export=download&id=0B6VhzidiLvjSOWdGM0tOX1lUNEk"
sent2vec_model = Doc2Vec.load(sent2vec_model_path)

# bern
def encode_text_bert(text):
    """Encode text using BERT tokenizer and obtain embeddings."""
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.pooler_output  # Use pooler_output for sentence-level embeddings

# bern
def retrieve_documents_bert(query, docs):
    """Retrieve and rank documents based on BERT-based similarity."""
    query_embedding = encode_text_bert(query)
    doc_scores = {}
    for doc_id, doc_text in docs.items():
        doc_embedding = encode_text_bert(doc_text)
        similarity_score = torch.nn.functional.cosine_similarity(query_embedding, doc_embedding)
        doc_scores[doc_id] = similarity_score.item()
    return doc_scores

# sent2vec
def preprocess_sent2vec(text):
    """Clean, tokenize, and preprocess the text."""
    # Tokenize the text
    tokens = word_tokenize(text)
    return tokens

# sent2vec
def encode_text_sent2vec(text):
    """Encode text using sent2vec model."""
    # Preprocess the text
    tokens = preprocess_sent2vec(text)
    # Encode the text
    vector = sent2vec_model.infer_vector(tokens)
    return vector

# sent2vec
def retrieve_documents_sent2vec(query, docs):
    """Retrieve and rank documents based on sent2vec similarity."""
    query_embedding = encode_text_sent2vec(query)
    doc_scores = {}
    for doc_id, doc_text in docs.items():
        doc_embedding = encode_text_sent2vec(doc_text)
        similarity_score = cosine_similarity(query_embedding, doc_embedding)
        doc_scores[doc_id] = similarity_score
    return doc_scores

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

import os
from preprocessing import preprocess
from indexing import create_inverted_index, compute_idf, compute_tf_idf, compute_document_lengths
from retrieval import retrieve_documents, rank_documents
from datetime import datetime

def load_queries(file_path):
    """Load queries from a specified file."""
    queries = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Assuming each line in the file is a separate query
            queries.append(preprocess(line.strip()))
    return queries

def load_documents(directory):
    """Load and preprocess documents from a specified directory."""
    docs = {}
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()
            docs[filename] = preprocess(text)  # Preprocess each document
    return docs

# Path to the directory where your documents are stored
docs_directory = 'AP_collection/coll/'
docs = load_documents(docs_directory)

# Create the inverted index from preprocessed documents
inverted_index = create_inverted_index(docs)

# Compute the total number of documents
doc_count = len(docs)

# Compute IDF scores
idf = compute_idf(inverted_index, doc_count)

# Compute TF-IDF scores for documents in the inverted index
tf_idf_index = compute_tf_idf(inverted_index, idf)

# Compute document lengths needed for cosine similarity calculation
doc_lengths = compute_document_lengths(tf_idf_index)

# Load and preprocess queries
queries_file_path = 'topics1-50.txt'
queries = load_queries(queries_file_path)

# # Process each query and rank documents
# for query in queries:
#     doc_scores = retrieve_documents(query, inverted_index, idf, doc_lengths, doc_count)
#     ranked_docs = rank_documents(doc_scores)
#     # You can now use ranked_docs as needed, e.g., for evaluation or displaying results.
#     # For instance, you could print the top 5 ranked document IDs for each query:
#     print("Query:", query)
#     print("Top 5 ranked documents:", ranked_docs[:5])
# Define a unique identifier for this run
run_name = f"IRS_{datetime.now().strftime('%Y%m%d_%H%M')}"

# Process each query, rank documents, and write to the Results file
with open('Results', 'w') as results_file:
    for i, query in enumerate(queries, start=1):
        doc_scores = retrieve_documents(query, inverted_index, idf, doc_lengths, doc_count)
        ranked_docs = rank_documents(doc_scores)
        for rank, (doc_id, score) in enumerate(ranked_docs[:1000], start=1):
            results_file.write(f"{i} Q0 {doc_id} {rank} {score:.4f} {run_name}\n")
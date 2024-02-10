import os
# Importing functions from other modules
from preprocessing import preprocess
from indexing import create_inverted_index, compute_tf_idf
# from retrieval import rank_documents  # Assuming you have this function implemented

def load_documents(directory):
    """Load and preprocess documents from a specified directory."""
    docs = {}
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):  # Adjust based on your file types
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                text = file.read()
                docs[filename] = preprocess(text)  # Preprocess each document
    return docs

# Adjust the directory path to where your documents are stored
docs_directory = 'path/to/your/documents'
docs = load_documents(docs_directory)

# Proceed with indexing and retrieval as previously outlined
inverted_index = create_inverted_index(docs)
doc_count = len(docs)
tf_idf_index = compute_tf_idf(inverted_index, doc_count)

# Implement query processing and ranking
# query = "example search query"
# ranked_docs = rank_documents(query, tf_idf_index)

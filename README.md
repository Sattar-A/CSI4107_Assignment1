# CSI4107_Assignment1

# Information Retrieval System README

## Team Members
- Member 1: Sattar Abdul, Student Number: [300156257]
- Member 2: Stephen Rioux, Student Number: [300175532]
- Member 3: Osa Ikhinmwin, Student Number: [300211931]

### Task Division (33% each member)
The works was divided equally between the members
- Member 1: Responsible for the 3 steps(preprocessing, indexing, retrieval)
- Member 2: Responsible for outputs and optimization
- Member 3: Responsible for setting up environments and overall project

## Functionality Overview
Our Information Retrieval (IR) system performs document indexing and query processing. It preprocesses text, creates an inverted index, computes TF-IDF scores, and retrieves and ranks documents based on cosine similarity with queries.

## Running the Program
1. Install Python and necessary libraries (e.g., `nltk`).
2. Place documents in the `AP_collection/coll/` directory or adjust the path 
3. Put the stop words and topics docs in the same directory
4. Run `main.py` with the command `python main.py`.

## Algorithms and Data Structures

### Preprocessing (Step 1)
- **Tokenization**: Splitting text into individual terms using regular expressions.
- **Stop Word Removal**: Filtering common words using a predefined list loaded from `StopWords.txt`.
- **Stemming**: Reducing words to their base or root form using NLTK's PorterStemmer.

### Indexing (Step 2)
- **Inverted Index**: Implemented using a defaultdict of dictionaries in Python, mapping terms to their document IDs and frequencies.
- **Term Frequency (TF)**: Counting the number of times each term appears in each document.
- **Document Frequency (DF)**: Calculated during inverted index creation by tracking the number of documents each term appears in.
- **TF-IDF Computation**: Employing the TF and DF values to calculate the importance of each term in the document corpus, which is used for ranking.
- **Document Vector Lengths**: Calculating the Euclidean norm of each document vector to normalize the cosine similarity scores during retrieval.

### Retrieval (Step 3)
- **Query Vectorization**: Transforming the query into a vector form based on the IDF scores from the indexed corpus.
- **Cosine Similarity**: Incrementally computed as query terms are processed to measure the relevance of documents to the query.
- **Ranking**: Sorting retrieved documents by their cosine similarity scores using a heap or sorted list data structure for efficiency.

### Evaluation Measures
- **Precision and Recall**: Standard evaluation metrics used to assess the effectiveness of the IR system, based on the relevance of the retrieved documents.


## Vocabulary and Results
- Vocabulary Size: [Insert size]
- Sample Tokens: [Insert 100 tokens here]
- First 10 Results for Query 1: [Insert results here]
- First 10 Results for Query 25: [Insert results here]

## Performance Evaluation
- Mean Average Precision (MAP) for 50 test queries: [Insert MAP score here]

Please replace the placeholders with your actual data and results.

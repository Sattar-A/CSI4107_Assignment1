# CSI4107_Assignment1

Sattar Abdul
Osa Ikhinmwin
Stephen Rioux

---

Assignment Summary:

**Course:** CSI4107 - Winter 2024

**Assignment:** Information Retrieval System

**Due Date:** February 11, 14:00

**Group Work:** Students are required to work in groups and submit via BrightSpace. Once one member submits, all members can see the submission.

**Task Overview:** Implement an Information Retrieval (IR) system based on the vector space model for a collection of documents. The system should retrieve relevant documents for a set of 50 test queries. The assignment consists of three main steps:

1. **Preprocessing (10 points):** Implement functions for tokenization, stopword removal, and optionally, stemming.
   
2. **Indexing (10 points):** Build an inverted index to facilitate fast access to documents.
   
3. **Retrieval and Ranking (10 points):** Use the inverted index to find documents containing query terms, compute cosine similarity scores, and rank documents based on similarity.

**Running the System:** Run the system on the set of 50 test queries and include the output in a file named "Results" with the specified format.

**Submission Instructions:**

- Write a README file including team members' names and student numbers, details of task division, functionality of programs, instructions for running them, explanations of algorithms and data structures used, and discussion of results.

- Produce a file named "Results" containing results for all test queries for the best run in the required format.

- Submit the assignment, including programs, README file, and Results file, as a zip file in BrightSpace (only one team member needs to submit).

- Do not include the initial text collection.

**Additional Notes:**

- Stopwords list and stemming (using Porter stemmer) are provided for preprocessing.

- Pseudo-relevance feedback loop and additional optimizations are encouraged.

- Students can use any IR system available on the Internet but should explain their usage in the report.

- Neural information retrieval methods (based on deep learning, transformers, BERT, or GPT-based models) are not allowed in this assignment.

- Mean Average Precision (MAP) score computed with trec_eval for the results on the 50 test queries should be included in the report.

- For queries/topics, use only the titles for one run and titles and descriptions for another run, and discuss which gives better results.

Overall, the assignment aims to implement an IR system, evaluate its performance, and provide insights into improving retrieval effectiveness.

import re
from nltk.stem import PorterStemmer

# Function to load stopwords from a file
def load_stopwords(file_path='StopWords.txt'):
    with open(file_path, 'r', encoding='utf-8') as file:
        stop_words = file.read().splitlines()
    return set(stop_words)

# Load stopwords
stop_words = load_stopwords()

# Initialize Porter Stemmer
stemmer = PorterStemmer()

def preprocess(text):
    """Clean, tokenize, remove stop words, and stem the text."""
    # Remove non-alphanumeric characters
    text = re.sub(r'\W+', ' ', text)
    # Tokenize by splitting the text
    tokens = text.lower().split()
    # Remove stopwords and stem
    tokens = [stemmer.stem(word) for word in tokens if word not in stop_words]
    return tokens

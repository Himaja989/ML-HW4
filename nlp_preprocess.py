# nlp_preprocess.py

import spacy

# Load the English language model (run "python -m spacy download en_core_web_sm" if not already installed)
nlp = spacy.load("en_core_web_sm")

# Input text
text = "John enjoys playing football while Mary loves reading books in the library."

# Process text with spaCy pipeline
doc = nlp(text)

# Define stopword list
stopwords = nlp.Defaults.stop_words

# Initialize list to hold final tokens
filtered_tokens = []

# Iterate through tokens and apply all steps
for token in doc:
    # Conditions:
    # 1. Token is not a stopword
    # 2. Token is alphabetic (no punctuation or digits)
    # 3. POS tag is NOUN or VERB
    if (token.text.lower() not in stopwords) and token.is_alpha and (token.pos_ in ["NOUN", "VERB"]):
        filtered_tokens.append(token.lemma_.lower())  # Lemmatize the token

# Output final result
print("Original Text:")
print(text)
print("\nProcessed Tokens (only Nouns and Verbs, lemmatized, no stopwords):")
print(filtered_tokens)

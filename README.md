# NLP Assignment – Part C

**Name:** Himaja Arabati  
**University:** University of Central Missouri  
**Course:** NLP – Fall 2025

---

## Q1. Text Preprocessing
**File:** nlp_preprocess.py  
Steps:
- Tokenization  
- Stopword removal  
- Lemmatization  
- Keep only nouns and verbs

**Input:**  
"John enjoys playing football while Mary loves reading books in the library."

**Output:**  
['enjoy', 'play', 'football', 'read', 'book', 'library']

**Run:**  
pip install spacy  
python -m spacy download en_core_web_sm  
python nlp_preprocess.py  

---

## Q2. Named Entity Recognition (NER)
**File:** ner_pronoun_check.py  
Performs:
- NER using spaCy  
- Detects pronouns and warns about ambiguity

**Input:**  
"Chris met Alex at Apple headquarters in California. He told him about the new iPhone launch."

**Output:**  
Shows entities (Chris, Alex, Apple, California, iPhone)  
Warning: Possible pronoun ambiguity detected!

**Run:**  
pip install spacy  
python -m spacy download en_core_web_sm  
python ner_pronoun_check.py  

---

**Files:**  
- nlp_preprocess.py  
- ner_pronoun_check.py  
- README.md  

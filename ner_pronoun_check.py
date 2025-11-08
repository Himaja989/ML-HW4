# ner_pronoun_check.py

import spacy

# Load spaCy English model (if not installed, run: python -m spacy download en_core_web_sm)
nlp = spacy.load("en_core_web_sm")

# Input text
text = "Chris met Alex at Apple headquarters in California. He told him about the new iPhone launch."

# Process text
doc = nlp(text)

# --- Named Entity Recognition ---
print("Named Entities, their labels, and explanations:\n")
for ent in doc.ents:
    print(f"{ent.text} --> {ent.label_} ({spacy.explain(ent.label_)})")

# --- Pronoun Ambiguity Detection ---
# Define pronouns to check for ambiguity
pronouns = {"he", "she", "they", "him", "her", "them"}

# Check if any pronouns are in the text
found_pronouns = [token.text.lower() for token in doc if token.text.lower() in pronouns]

if found_pronouns:
    print("\n⚠️ Warning: Possible pronoun ambiguity detected!")
    print(f"Pronouns found: {set(found_pronouns)}")
else:
    print("\nNo pronoun ambiguity detected.")

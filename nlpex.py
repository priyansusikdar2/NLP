# Import necessary libraries
import spacy
from spacy import displacy
import pandas as pd

# === LOAD spaCy ENGLISH MODEL ===
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading 'en_core_web_sm' model...")
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# === SAMPLE TEXT ===
text = """
Amazon announced its quarterly earnings on July 30, 2023. 
CEO Andy Jassy said the company is investing $4 billion in AI technology. 
Google, based in Mountain View, California, also shared its financial report. 
The 2024 Summer Olympics will be held in Paris, France.
"""

# === PROCESS TEXT ===
doc = nlp(text)

# === FUNCTION TO EXTRACT ENTITIES ===
def extract_entities(doc):
    entities = []
    for ent in doc.ents:
        entities.append({
            'Entity': ent.text,
            'Label': ent.label_,
            'Explanation': spacy.explain(ent.label_)
        })
    return pd.DataFrame(entities)

# === EXTRACT ENTITIES INTO A DATAFRAME ===
entities_df = extract_entities(doc)

# === DISPLAY IN TERMINAL ===
print("Extracted Named Entities:\n")
print(entities_df)

# === SAVE TO CSV ===
entities_df.to_csv("extracted_entities.csv", index=False)
print("\nEntities saved to 'extracted_entities.csv'")

# === OPTIONAL: SAVE VISUALIZATION TO HTML (since displacy.render doesn't show in VS Code) ===
html = displacy.render(doc, style="ent", page=True)
with open("ner_visualization.html", "w", encoding="utf-8") as f:
    f.write(html)
print("\nNamed Entity visualization saved to 'ner_visualization.html'")

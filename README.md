# Named Entity Recognition (NER) with spaCy

This project demonstrates how to perform **Named Entity Recognition (NER)** using the `spaCy` library in Python. The script processes a sample text, extracts entities like names, dates, organizations, and locations, and saves the results in a CSV file and an HTML visualization.

---

## 📋 Features

- Uses spaCy's `en_core_web_sm` model for entity recognition
- Extracts entities into a clean `pandas` DataFrame
- Automatically downloads the model if not present
- Saves extracted entities to a CSV file
- Generates a standalone HTML file for visualizing NER results

---

## 🛠 Requirements

Install the dependencies:

```bash
pip install spacy pandas
python -m spacy download en_core_web_sm
```

---

## 🚀 How to Run

1. **Save the script** to a `.py` file, e.g., `ner_extractor.py`
2. **Run the script** in VS Code or your terminal:

```bash
python ner_extractor.py
```

3. **Output:**
   - `extracted_entities.csv`: CSV of all named entities with labels and explanations
   - `ner_visualization.html`: Visual NER output (open this in your browser)

---

## 🧠 Sample Extracted Entities

| Entity               | Label     | Explanation                 |
|----------------------|-----------|-----------------------------|
| Amazon               | ORG       | Companies, agencies, etc.   |
| July 30, 2023        | DATE      | Absolute or relative dates  |
| Andy Jassy           | PERSON    | People, including fictional |
| Mountain View        | GPE       | Countries, cities, states   |
| 2024 Summer Olympics | EVENT     | Named hurricanes, wars, etc.|
| Paris, France        | GPE       | Countries, cities, states   |

---

## 📂 Output Files

- `extracted_entities.csv`: Tabular data of entities
- `ner_visualization.html`: Color-coded entity visualization (open in browser)

---

## 📌 Notes

- `displacy.render(..., jupyter=True)` is replaced with an HTML export for compatibility with VS Code.
- Modify the `text` variable to analyze your own custom content.

---

## 📧 Contact

For questions or improvements, feel free to open an issue or contribute.

```

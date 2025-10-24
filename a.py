

import spacy
nlp = spacy.load("en_core_web_sm")

test_text = """
I want to buy an iPhone 12 Pro Max from Apple.
Show me the latest Samsung Galaxy phone.
I am looking for a pair of Nike Air Max shoes in size 10.
"""

doc = nlp(test_text)


for  ent in doc.ents:
    print(f"{ent.text}, Label: {ent.label_}")

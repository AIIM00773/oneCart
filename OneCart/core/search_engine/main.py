
from matcher import nlp, matcher

text = "Show me vivo smartphones under 20000 on phoneplace kenya"
doc = nlp(text)

matches = matcher(doc)
for match_id, start, end in matches:
    label = nlp.vocab.strings[match_id]
    span = doc[start:end]
    print(f"{label}: {span.text}")


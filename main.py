import spacy
from spacy import displacy

def main():
    # Load  spaCy pipeline (no custom rules)
    nlp = spacy.load("en_core_web_sm")

    with open("logs.txt", "r", encoding="utf-8") as f:
        text = f.read()


    # Run spaCy
    doc = nlp(text)

    # Print pipeline components (what's inside the model)
    print("Pipeline:", nlp.pipe_names)
    print("-" * 60)

    # Print named entities
    print("ENTITIES (text | label):")
    for ent in doc.ents:
        print(f"{ent.text} | {ent.label_}")
    print("-" * 60)

    # Print a few noun chunks (useful to see groups like 'a group of teenagers')
    print("NOUN CHUNKS (first 50):")
    for i, chunk in enumerate(doc.noun_chunks):
        if i >= 50:
            break
        print(chunk.text)
    print("-" * 60)

    # Print first 10 sentences
    print("SENTENCES (first 10):")
    for i, sent in enumerate(doc.sents):
        if i >= 10:
            break
        print(f"{i+1}. {sent.text.strip()}")
    print("-" * 60)

    
    print("TOKENS (first 50):")
    for token in doc[:50]:
        print(token.text, token.pos_, token.dep_)
    print("-" * 60)
    

    # Save an HTML visualization of entities
    html = displacy.render(doc, style="ent", page=True)
    with open("entities.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Saved entity highlight to: entities.html")




if __name__ == "__main__":
    main()


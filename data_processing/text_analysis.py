#takes each word and checks if it is a name, location(adress or street) or vehicle(make,model,colour)

import spacy

def process_file(file):
    nlp = spacy.load("en_core_web_sm")
    file_text = ""
    
    for chunk in file.chunks():
        file_text += chunk
    
    doc = nlp(file_text)






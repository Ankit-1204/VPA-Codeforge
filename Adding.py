
# # Check if the model is already downloaded
# if model_name not in spacy.util.info()["installed"]:
#     # Download the model
#     spacy.cli.download(model_name)

# # Load the model

import spacy
import os
from date import get_date
from timeconv import get_time
import pandas as pd
from spacy.matcher import PhraseMatcher
from send import mail

# Function to extract DATE and TIME entities from user input
def adder(user_name,user_input,nlp):
    doc = nlp(user_input)
    date_time_entities = {
        ent.label_: ent.text
        for ent in doc.ents
        if ent.label_ in ["DATE", "TIME"]
    }

    date_entity = get_date(date_time_entities.get("DATE", None))
    time_entity = get_time(date_time_entities.get("TIME", None))

    csv_file_path = "users.csv"
    df = pd.read_csv(csv_file_path)
    names = df['username'].tolist()

    def is_user_name(word):
        return word.lower() in [name.lower() for name in names]
    
    
    # Add more event names as needed
    event_names = ["meeting", "presentation", "interview", "lunch", "deadline", "team call", "review"]
    

# Process the input text
    
    doc = nlp(user_input)

# Initialize a PhraseMatcher for event names
    matcher = PhraseMatcher(nlp.vocab)
    event_patterns = [nlp(event) for event in event_names]
    matcher.add("EventMatcher", None, *event_patterns)

# Extract user names and event names
    user_names_found = [token.text for token in doc if is_user_name(token.text)]
    user_names_found.append(user_name)
    
    matches = matcher(doc)
    if matches:
        event_names_found = [doc[start:end].text for match_id, start, end in matches]
    else:
        event_names_found = ["Reminder"]
    
    mail(date_entity,time_entity,user_names_found,event_names_found)
    return date_entity,time_entity,user_names_found,event_names_found

# Example usage


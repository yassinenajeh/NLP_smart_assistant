from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


INTENTS = {

    0: "EXPLAIN",

    1: "SUMMARIZE",

    2: "EXERCISES",

    3: "CORRECT",

    4: "TRANSLATE",

    5: "SOLVE",

    6: "QUESTION",

    7: "OTHER"

}

tokenizer = AutoTokenizer.from_pretrained(

    "./intent_model"

)

model = AutoModelForSequenceClassification.from_pretrained(

    "./intent_model"

)


def detect_intent (text):

    inputs = tokenizer(text, return_tensors="pt")

    output = model(**inputs)

    logits = output.logits

    predicted_id = logits.argmax(dim=1).item()

    return INTENTS[predicted_id]
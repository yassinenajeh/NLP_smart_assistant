import pandas as pd
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from datasets import Dataset
from transformers import Trainer
from transformers import TrainingArguments


model = AutoModelForSequenceClassification.from_pretrained(

    "distilbert-base-multilingual-cased",

    num_labels=8

)

tokenizer = AutoTokenizer.from_pretrained(

    "distilbert-base-multilingual-cased"

)

def train():

    dataset = pd.read_csv("dataset/train.csv")

    texts = dataset["text"].tolist()

    labels = dataset["label"].tolist()

    encoded_texts = tokenizer(

        texts,

        padding=True,

        truncation=True

    )

    train_dataset = Dataset.from_dict({

        "input_ids": encoded_texts["input_ids"],

        "attention_mask": encoded_texts["attention_mask"],

        "labels": labels

    })

    validation_dataset = valid()

    training_args = TrainingArguments(

        output_dir="./intent_model",

        num_train_epochs=3,

        per_device_train_batch_size=8,

        per_device_eval_batch_size=8,

        eval_strategy="epoch",

        save_strategy="epoch",

        logging_strategy="epoch",

        load_best_model_at_end=True

    )

    trainer = Trainer(

        model=model,

        args=training_args,

        train_dataset=train_dataset,

        eval_dataset=validation_dataset

    )
   
    trainer.train()

    trainer.save_model("./intent_model")

    tokenizer.save_pretrained("./intent_model")

    return trainer, tokenizer

def valid():

    dataset = pd.read_csv("dataset/validation.csv")
    
    texts = dataset["text"].tolist()
    
    labels = dataset["label"].tolist()
    
    encoded_texts = tokenizer(
    
        texts,
    
        padding=True,
    
        truncation=True
    
    )
    
    validation_dataset = Dataset.from_dict({
    
        "input_ids": encoded_texts["input_ids"],
    
        "attention_mask": encoded_texts["attention_mask"],
    
        "labels": labels
    
    })

    return validation_dataset

def test():

    dataset = pd.read_csv("dataset/test.csv")

    texts = dataset["text"].tolist()

    labels = dataset["label"].tolist()

    encoded_texts = tokenizer(

        texts,

        padding=True,

        truncation=True

    )

    test_dataset = Dataset.from_dict({

        "input_ids": encoded_texts["input_ids"],

        "attention_mask": encoded_texts["attention_mask"],

        "labels": labels

    })

    trainer = Trainer(

        model=model

    )

    results = trainer.predict(test_dataset)

    predictions = results.predictions.argmax(axis=1)

    labels = results.label_ids

    correct = (predictions == labels).sum()

    accuracy = correct / len(labels)

    print(f"Accuracy : {accuracy:.2%}")

    for intent in range(8):

        total = (labels == intent).sum()

        correct = ((predictions == intent) & (labels == intent)).sum()

        accuracy = correct / total

        print(f"Intent {intent} : {accuracy:.2%} ({correct}/{total})")

    for i in range(len(labels)):

        if predictions[i] != labels[i]:

            print()
            print(f"Text : {texts[i]}")
            print(f"True : {labels[i]}")
            print(f"Predicted : {predictions[i]}")

train()
test()
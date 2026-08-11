# NLP Smart Assistant

Project completed in 2025 – documented here for portfolio purposes.

## 📌 Overview

NLP Smart Assistant is a *Python* application designed to understand user requests and generate appropriate responses using Natural Language Processing and transformer-based AI models.

The project combines several pretrained and fine-tuned models into a single application with a graphical user interface.

The main goal of the project was to understand how different NLP components can be combined to create a complete AI assistant.

## 📸 Preview

- **Main interface**
<img width="655" height="914" alt="Screenshot 1" src="https://github.com/user-attachments/assets/97d05dc0-0c43-4362-9eae-2d081fa0c78b" />

- **Answering AI**
<img width="650" height="951" alt="Screenshot 2" src="https://github.com/user-attachments/assets/50b62da5-0ee3-42f8-ad8c-965fa3b5e890" />

- **Assistant response**
<img width="658" height="928" alt="Screenshot 3" src="https://github.com/user-attachments/assets/d6027d9b-305a-46ae-89fd-1a4314e5ffcf" />

## ⚙️ How it works

The assistant processes each message through the following pipeline:

```text
User message
     ↓
Language Detection
     ↓
Intent Classification
     ↓
Task Selection
     ↓
Text Generation
     ↓
Assistant Response
```

## 💻 Technologies

| Category                        | Technology                |
| ------------------------------- | ------------------------- |
| **Programming Language**        | Python 3                  |
| **User Interface (UI)**         | CustomTkinter             |
| **Intent Classification Model** | DistilBERT multilingual   |
| **Text Generation Model**       | Qwen2.5-1.5B-Instruct     |
| **AI Framework**                | PyTorch                   |
| **NLP Library**                 | Hugging Face Transformers |
| **Dataset Management**          | Hugging Face Datasets     |
| **Data Processing**             | Pandas                    |

## ✨ Features

- 🧠 Custom-trained intent classification
- 🌐 Multilingual input and responses
- 🤖 AI-generated responses
- 📝 8 different user intents
- 📊 Model evaluation on a dedicated test dataset
- 🎯 Per-intent accuracy evaluation
- 🔍 Display of incorrectly classified test examples
- 💬 Conversation-style graphical interface
- 🇬🇧 English interface
- 🇫🇷 French interface
- 🔄 Reset functionality
- 🧪 Dedicated test messages for different tasks
- ⚡ Asynchronous response generation

## 🧠 Intent Classification

One of the main components of the project is a custom intent classification system designed to determine what the user is asking the assistant to do.

The classifier uses *DistilBERT multilingual* (`distilbert-base-multilingual-cased`), which was fine-tuned specifically for this project on a custom dataset.

### 🎯 Intent Categories

The model classifies each user request into one of 8 intents :

| ID | Intent | Description |
|---:|---|---|
| 0 | `EXPLAIN` | Explain a concept, topic or idea |
| 1 | `SUMMARIZE` | Summarize information |
| 2 | `EXERCISES` | Generate or provide exercises |
| 3 | `CORRECT` | Correct a text, sentence or answer |
| 4 | `TRANSLATE` | Translate text |
| 5 | `SOLVE` | Solve a problem or equation |
| 6 | `QUESTION` | Answer a specific question |
| 7 | `OTHER` | Handle requests outside the other categories |

The classification process can be summarized as :

```text
User message
     ↓
Tokenization
     ↓
DistilBERT
     ↓
Logits
     ↓
Predicted intent
```

### 🤖 Model Training

The pretrained `distilbert-base-multilingual-cased` model was fine-tuned for this specific classification task.

The training configuration used :

- **8 intent classes**
- **3 training epochs**
- **Batch size: 8**
- **Validation after each epoch**
- **Best model automatically loaded after training**

The validation loss decreased throughout training :

| Epoch | Validation Loss |
| ----: | --------------: |
|     1 |          0.5935 |
|     2 |          0.3140 |
|     3 |          0.2993 |

### 📚 Dataset

A custom dataset containing **800 labelled examples** was created specifically for the project.

Each example contains :
- The user's text
- Its corresponding intent label

The dataset was divided into separate training, validation and test sets :

```text
800 examples
     │
     ├── Training set
     │
     ├── Validation set
     │
     └── Test set
```

The dataset was also refined after analyzing the model's errors in order to improve the distinction between semantically similar intents, particularly `EXPLAIN` and `QUESTION`.

### 📊 Evaluation

The final model achieved an overall **96.25% accuracy** on the test dataset.

| Intent      | Accuracy |
| ----------- | -------: |
| `EXPLAIN`   |      80% |
| `SUMMARIZE` |     100% |
| `EXERCISES` |     100% |
| `CORRECT`   |     100% |
| `TRANSLATE` |     100% |
| `SOLVE`     |     100% |
| `QUESTION`  |     100% |
| `OTHER`     |      90% |

The evaluation script also identifies incorrectly classified examples, making it possible to analyze the model's weaknesses and improve the dataset.

Most of the remaining errors occur between semantically similar requests, especially short questions that can reasonably be interpreted as either an `EXPLAIN` or a `QUESTION` request.

The classifier is therefore not only evaluated through its overall accuracy, but also through per-intent accuracy and error analysis.

## 📁 Project Structure

```
AI-Smart-Assistant/
│
├── dataset/
│   ├── train.csv
│   ├── validation.csv
│   └── test.csv
│
├── screenshots/
│   ├── Screenshot 1.png
│   ├── Screenshot 2.png
│   └── Screenshot 3.png
│
├── test_messages/
│   ├── 01_math_request.txt
│   ├── 02_explanation.txt
│   ├── 03_french_request.txt
│   ├── 04_exercises.txt
│   ├── 05_translation.txt
│   ├── 06_correction.txt
│   ├── 07_summary.txt
│   ├── 08_question.txt
│   ├── 09_other.txt
│   └── 10_multiple_messages.txt
│
├── assistant.py
├── generator.py
├── intent.py
├── interface.py
├── language.py
├── main.py
├── requirements.txt
├── train_intent.py
├── translations.py
├── .gitignore
└── README.md
```

### 📄 Main Files

**`main.py`**  
Starts the application.

**`interface.py`**  
Contains the graphical interface and handles user interaction, messages, buttons, language switching and reset functionality.

**`assistant.py`**  
Connects the different components of the assistant and manages the processing pipeline.

**`language.py`**  
Handles automatic language detection.

**`intent.py`**  
Loads the trained *DistilBERT* model and predicts the intent of the user's message.

**`generator.py`**
Loads the *Qwen* model and generates the assistant's responses.

**`train_intent.py`**
Contains the dataset preparation, training and evaluation process for the intent classification model.

**`translations.py`**
Contains the English and French interface translations.

**`requirements.txt`**
Lists the *Python* packages required to run the project.

## 🚀 Installation

Clone the repository and install the required dependencies :

```bash
pip install -r requirements.txt
```

Then start the application with :

```bash
python main.py
```

The required AI models are loaded when they are needed by the application.

## 🧪 Testing

The **'test_messages'** folder contains several example messages that can be copied into the application to test different parts of the assistant.

The examples cover :
- Mathematical requests
- Explanations
- French requests
- Exercise generation
- Translation
- Text correction
- Summarization
- Questions
- Unrelated requests
- Multiple messages

These tests make it possible to verify both the intent classification and the final response generated by the assistant.

## ⚠️ Limitations

The assistant does not understand user requests with perfect accuracy.

The intent classifier can occasionally confuse semantically similar requests, particularly short questions that could belong to either **'EXPLAIN'** or **'QUESTION'**.

The generated responses are also produced by an AI model and may therefore contain:
- Incorrect information
- Unnecessary details
- Formatting issues
- Mathematical expressions that may not always be displayed correctly

Response generation can also take several seconds depending on the computer's hardware.

The assistant should therefore be considered an educational AI project rather than a system providing guaranteed correct answers.

## 🔬 What I Learned

This project allowed me to work on several important aspects of Natural Language Processing and Machine Learning.

Through this project, I learned how to :
- Prepare and label a custom NLP dataset
- Tokenize text for transformer models
- Use pretrained transformer models
- Fine-tune DistilBERT for an intent classification task
- Understand model logits and predictions
- Evaluate a classification model using separate validation and test datasets
- Analyze classification errors and improve the dataset accordingly
- Combine multiple AI models into a single application
- Implement asynchronous AI text generation
- Create a graphical interface for an AI application
- Test an AI application using predefined test cases

## 🔮 Future Improvements

Possible improvements include :
- 📚 Increasing the size of the intent dataset
- 🧠 Adding more intent categories
- 🎯 Further improving the distinction between semantically similar intents
- ⚡ Reducing response generation time
- 📐 Improving mathematical expression rendering

## 👨‍💻 Author

**Yassine Najeh**

Computer Engineering student interested in embedded systems, Artificial Intelligence and hardware-software integration.

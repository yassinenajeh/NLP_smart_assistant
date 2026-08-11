# NLP Smart Assistant

Project completed in 2025 – documented here for portfolio purposes.

## 📌 Overview

NLP Smart Assistant is a Python application designed to understand user requests and generate appropriate responses using Natural Language Processing and transformer-based AI models.

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
Loads the trained DistilBERT model and predicts the intent of the user's message.

**`generator.py`**
Loads the Qwen model and generates the assistant's responses.

**`train_intent.py`**
Contains the dataset preparation, training and evaluation process for the intent classification model.

**`translations.py`**
Contains the English and French interface translations.

**`requirements.txt`**
Lists the Python packages required to run the project.

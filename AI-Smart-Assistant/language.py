from transformers import pipeline


language_detector = pipeline(
    "text-classification",
    model="papluca/xlm-roberta-base-language-detection"
)


def detect_language(text):

    language = language_detector(text)

    return language[0]["label"]
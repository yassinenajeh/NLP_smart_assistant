from language import detect_language
from intent import detect_intent
from generator import generate_answer


def process(text):

        language = detect_language(text)

        intent = detect_intent(text)

        answer = generate_answer(text, language, intent)

        return answer
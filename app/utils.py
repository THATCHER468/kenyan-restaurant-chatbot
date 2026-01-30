import os
import json
import pickle as pkl
from copyreg import pickle


import random
import string

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "model", "chatbot_model.pkl")
VECT_PATH = os.path.join(BASE_DIR, "model", "vectorizer.pkl")
INTENTS_PATH = os.path.join(BASE_DIR, "data", "intents.json")

model = pkl.load(open(MODEL_PATH, "rb"))
vectorizer = pkl.load(open(VECT_PATH, "rb"))

with open(INTENTS_PATH, encoding="utf-8") as f:
    intents = json.load(f)

# Load model & vectorizer
model = pkl.load(open(MODEL_PATH, "rb"))
vectorizer = pkl.load(open(VECT_PATH, "rb"))

with open(INTENTS_PATH, encoding="utf-8") as f:
    intents = json.load(f)


def clean_text(text):
    text = text.lower()
    return "".join([c for c in text if c not in string.punctuation])

    #updated to the cide below
import random

def get_response(message, threshold=0.6):
    """
    Returns a chatbot response for Kenyan restaurants.
    Features:
    - Handles greetings separately (Hi, Hello, Habari, Sasa, Sheng phrases)
    - Uses model confidence threshold
    - Falls back safely if unsure
    """

    # 1️⃣ Clean the message
    message_clean = clean_text(message)

    # 2️⃣ Pre-handle greetings (short/common phrases)
    greetings = [
        "hi", "hello", "hey", "sasa", "habari", "yo", "hujambo", "good morning", "good afternoon"
    ]
    if message_clean in greetings:
        for intent in intents["intents"]:
            if intent["tag"] == "greeting":
                return random.choice(intent["responses"])

    # 3️⃣ ML-based intent prediction
    vect = vectorizer.transform([message_clean])
    probs = model.predict_proba(vect)[0]
    tags = model.classes_

    max_prob_index = probs.argmax()
    max_prob = probs[max_prob_index]
    tag = tags[max_prob_index]

    # 4️⃣ Decide response
    if max_prob >= threshold:
        # High confidence → return matching intent
        for intent in intents["intents"]:
            if intent["tag"] == tag:
                return random.choice(intent["responses"])
    else:
        # Low confidence → fallback
        for intent in intents["intents"]:
            if intent["tag"] == "fallback":
                return random.choice(intent["responses"])
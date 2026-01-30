## Kenyan Restaurant Chatbot
A simple AI chatbot for Kenyan restaurants, built with FastAPI, Python, and TF-IDF + Logistic Regression.
Supports English, Swahili, and Sheng for greetings, menu, hours, location, drinks, and desserts.

## Features
🗣️ Bilingual support: English + Swahili/Sheng
🍽️ Menu queries: food, drinks, desserts
⏰ Opening hours & 📍 location queries
🤖 Fallback for unknown queries
💻 Interactive local chat script
⚡ Easy retraining for new menu items or phrases

## Project Structure

restaurant-chatbot/
│
├─ app/
│   ├─ main.py        # FastAPI server
│   └─ utils.py       # Helper functions (get_response, text cleaning)
│
├─ model/
│   ├─ train.py       # Script to train the model
│   ├─ chatbot_model.pkl
│   └─ vectorizer.pkl
│
├─ data/
│   └─ intents.json   # Chatbot dataset (greetings, menu, hours, location)
│
└─ run_chatbot.py      # Interactive chat script

## Requirements
1. Python 3.10+

2. Install dependencies:
# Bash
pip install fastapi uvicorn scikit-learn pandas numpy requests

## Setup & Run Locally
1. Update dataset (optional)
Edit data/intents.json to add new menu items, drinks, desserts, or local phrases (Swahili/Sheng).
2. Train the model
# Bash
cd model
python train.py

Generates chatbot_model.pkl and vectorizer.pkl
Must be rerun anytime you update intents.json

3. Start the FastAPI server
# Bash
cd ..
python -m uvicorn app.main:app --reload

The server will run at http://127.0.0.1:8000
Swagger UI: http://127.0.0.1:8000/docs

4. Run the server + chat locally in one command
In a new terminal:
# Bash
python run_chatbot.py

Type messages naturally
Type exit or quit to end the chat

Example:
You: Hi
Bot: Hello 😊 Welcome to our restaurant!
You: Menu please
Bot: Hii ndiyo menyu yetu 🍽️: Pilau, Kuku Fry, Beef Stew, Chapati, Chips.

## How it works
1. User message → FastAPI POST /chat
2. Message cleaned & vectorized → TF-IDF
3. Model predicts intent (Logistic Regression)
4. Response selected from intents.json
5. Fallback used if confidence < threshold

## Tips for Kenyan context
. Add common Sheng phrases for menu requests, e.g., "Nipe chakula leo", "Menyu iko wapi bro?"
. Retrain the model after adding new patterns
. Keep responses friendly & bilingual for local users

## Future Improvements
. Multi-turn conversation (remember previous messages)
. Integration with WhatsApp or web chat widget
. Live deployment with HTTPS (Railway / Heroku)
. Adding order tracking & payment options


## Authur 
Maggie lol
import subprocess
import time
import requests

# Step 1: Start FastAPI server in background
print("🟢 Starting FastAPI server...")
server = subprocess.Popen(
    ["python", "-m", "uvicorn", "app.main:app", "--reload"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

# Give the server a few seconds to start
time.sleep(3)

print("✅ Server should be running! Starting chat...")

# Step 2: Start interactive chat
url = "http://127.0.0.1:8000/chat"

try:
    while True:
        message = input("You: ").strip()
        if message.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        response = requests.post(url, json={"message": message})
        data = response.json()
        print("Bot:", data.get("reply", "🤔 No reply"))

finally:
    # Step 3: Stop the server when chat ends
    print("\n🛑 Shutting down server...")
    server.terminate()
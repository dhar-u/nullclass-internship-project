import json
from datetime import datetime

def log_interaction(user_input, bot_response, topic="general", rating=None):
    log_entry = {
        "timestamp": datetime.now().isoformat(),   # Records current date and time
        "user_input": user_input,                  # What the user asked
        "bot_response": bot_response,              # What the bot replied
        "topic": topic,                            # Optional topic tag like "greeting"
        "rating": rating                           # Optional user rating (e.g., 1-5 stars)
    }

    # Open or create a file to store this data line by line
    with open("chat_logs.json", "a") as f:
        f.write(json.dumps(log_entry) + "\n")

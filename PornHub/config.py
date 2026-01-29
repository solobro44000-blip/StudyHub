import os
from typing import List

# Read from Environment Variables (set these in Render later)
API_ID: int = int(os.environ.get("API_ID", "0"))
API_HASH: str = os.environ.get("API_HASH", "")
TOKEN: str = os.environ.get("TOKEN", "")
# Log Chat ID (Read from Environment, defaults to 0 if not set)
# We wrap it in int() because chat IDs must be integers
try:
    log_chat: int = int(os.environ.get("LOG_CHAT", "0"))
except ValueError:
    log_chat: int = 0
# ... rest of your code (log_chat, sub_chat, etc.) ...

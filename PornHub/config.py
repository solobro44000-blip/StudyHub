import os
from typing import List

# Read from Environment Variables (set these in Render later)
API_ID: int = int(os.environ.get("API_ID", "0"))
API_HASH: str = os.environ.get("API_HASH", "")
TOKEN: str = os.environ.get("TOKEN", "")
log_chat: int = -5256755543
# ... rest of your code (log_chat, sub_chat, etc.) ...

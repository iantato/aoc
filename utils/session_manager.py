import os
from .constants import SESSION_FILE

def load_session() -> str:
    """Load AOC session cookies from cache file"""
    if not os.path.exists(SESSION_FILE):
        raise FileNotFoundError(f"Session cache file '{SESSION_FILE}' not found. Please create it with your session cookies.")

    session = open(SESSION_FILE).read().strip()
    if not isinstance(session, str) or not session:
        raise TypeError("Session cookies are not valid. Please check the session file.")
    return session
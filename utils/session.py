import os
from .logs import log

def load_session() -> str:
    """Load AOC session cookies from cache file"""
    session_cache_file = '.session.lock'
    if not os.path.exists(session_cache_file):
        log(f"Session cache file '{session_cache_file}' not found. Creating a new one.", level="WARNING")
        session = input("Please enter your session cookies: ").strip()
        with open(session_cache_file, 'w') as f:
            f.write(session)
        log("Session cookies saved successfully.", level="INFO")

    session = open(session_cache_file).read().strip()
    if not isinstance(session, str) or not session:
        log("Session cookies are not valid. Please check the session file.", level="ERROR")
        raise TypeError("Session cookies are not valid. Please check the session file.")
    log("Session cookies loaded successfully.", level="INFO")
    return session
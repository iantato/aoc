import os
from .constants import PROBLEMS_DIR

def create_problem_directory(year: str, day: str) -> str:
    """
    Create necessary directories for the AOC problem.

    Args:
        year (str): The year of the AOC challenge.
        day (str): The day of the AOC challenge.

    Returns:
        str: The path to the created problem directory.
    """

    dest_day = os.path.join(PROBLEMS_DIR, year, f'day_{int(day):02}')
    os.makedirs(dest_day, exist_ok=True)

    return dest_day
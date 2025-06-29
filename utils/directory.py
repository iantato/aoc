import os
from .logs import Colors, log

def create_directories(year: str, day: str):
    """Create necessary directories for AOC problem and tests"""
    dest_day = os.path.join('problems', year, f'day_{int(day):02}')
    dest_test = os.path.join('tests', year)

    if os.path.isdir(dest_day):
        log(f'Destination directory [{Colors.colorize(dest_day, Colors.PURPLE)}] already exists.', level="WARNING")
    else:
        os.makedirs(dest_day, exist_ok=True)
        log(f'Destination directory [{Colors.colorize(dest_day, Colors.PURPLE)}] created successfully.', level="INFO")

    if not os.path.isdir(dest_test):
        os.makedirs(dest_test, exist_ok=True)
        log(f'Test directory [{Colors.colorize(dest_test, Colors.PURPLE)}] created successfully.', level="INFO")

    return dest_day, dest_test
from .session import load_session
from .directory import create_directories
from .parsers import parse_day_description, parse_input_data

def collect_aoc_data(day: str, year: str):
    """Collect AOC data for given day and year"""
    session = load_session()
    dest_day, dest_test = create_directories(year, day)

    URL = 'https://adventofcode.com'
    day_url = f'{URL}/{year}/day/{day}'

    parse_day_description(day_url, session, dest_day, year, day)
    parse_input_data(day_url, session, dest_day, year, day)
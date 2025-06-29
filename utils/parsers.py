import os
import requests
from bs4 import BeautifulSoup
from .constants import USER_AGENT

def parse_day_desc(day_url: str, session: str, year: str, day: str, dest_day: str) -> None:
    """
    Parse the day description from the AOC website.
    It saves the description to a README markdown file.

    Args:
        day_url (str): The URL for the specific day.
        session (str): The session cookie for authentication.
        year (str): The year of the AOC challenge.
        day (str): The day of the AOC challenge.
        dest_day (str): The destination directory to save the description.
    """

    # Initialize everything needed for parsing with BeautifulSoup.
    headers = {'User-Agent': USER_AGENT}
    response = requests.get(day_url, cookies={'session': session}, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    instructions = soup.find_all('article', attrs={'class': 'day-desc'})

    day_desc_title = soup.select_one('.day-desc h2')
    title_text = day_desc_title.get_text(strip=True) if day_desc_title else ""
    day_desc_path = os.path.join(dest_day, 'README.md')

    # Write the parsed description to a markdown file.
    with open(day_desc_path, 'w', encoding='utf-8') as md:
        md.write(f'# {title_text}\n\n')
        for part, instruction in enumerate(instructions, start=1):
            if part == 2:
                md.write('### --- Part 2 ---\n\n')
            for article in instruction: # type: ignore
                match article.name:
                    case 'p':
                        md.write(f'{article.get_text()}\n\n')
                    case 'pre':
                        md.write(f'```shell\n{article.get_text()}```\n\n')
    md.close()

def parse_user_input(day_url: str, session: str, dest_day: str) -> None:
    """
    Parse the user input data from the AOC website.
    It saves the input data to an input.txt file.

    Args:
        day_url (str): The URL for the specific day.
        session (str): The session cookie for authentication.
        dest_day (str): The destination directory to save the input data.
    """

    # Initialize everything needed for parsing with BeautifulSoup.
    headers = {'User-Agent': USER_AGENT}
    input_path = os.path.join(dest_day, 'input.txt')
    response = requests.get(f'{day_url}/input', cookies={'session': session}, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Write the parsed input data to a text file.
    with open(input_path, 'w', encoding='utf-8') as input_file:
        input_data = soup.get_text(strip=True)
        input_file.write(input_data)
    input_file.close()

def parse_test_input(day_url: str, session: str, dest_test: str) -> None:
    """
    Parse the test input data from the AOC website.
    It saves the test input data to a test_input.txt file.

    Args:
        day_url (str): The URL for the specific day.
        session (str): The session cookie for authentication.
        dest_test (str): The destination directory to save the test input data.
    """

    # Initialize everything needed for parsing with BeautifulSoup.
    headers = {'User-Agent': USER_AGENT}
    test_input_path = os.path.join(dest_test, 'test_input.txt')

    response = requests.get(day_url, cookies={'session': session}, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    instructions = soup.find('article', attrs={'class': 'day-desc'})

    # Write the parsed test input to a text file.
    with open(test_input_path, 'w', encoding='utf-8') as test_input_file:
        for section in instructions: # type: ignore
            if section.name == 'p' and 'example' in section.get_text().lower():
                next_section = section.find_next_sibling()
                if next_section and next_section.name == 'pre':
                    pre_content = next_section.get_text(strip=True)
                    test_input_file.write(pre_content)
                    break
    test_input_file.close()
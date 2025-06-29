import os
import requests
from bs4 import BeautifulSoup
from .logs import Colors, log

def parse_day_description(day_url: str, session: str, dest_day: str, year: str, day: str):
    """Parse and save day description to README.md"""
    headers = {'User-Agent': 'AoC by Christian Mark Francisco'}
    response = requests.get(day_url, cookies={'session': session}, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    instructions = soup.find_all('article', attrs={'class': 'day-desc'})

    day_desc_title = soup.select_one('.day-desc h2')
    title_text = day_desc_title.get_text(strip=True) if day_desc_title else ""
    day_desc_path = os.path.join(dest_day, 'README.md')

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
            log(f'Description for {Colors.colorize(year, Colors.BOLD)}-{Colors.colorize(day, Colors.BOLD)} for Part {part} collected successfully!',
                level="INFO")

def parse_input_data(day_url: str, session: str, dest_day: str, year: str, day: str):
    """Parse and save input data to input.txt"""
    headers = {'User-Agent': 'AoC by Christian Mark Francisco'}
    input_path = os.path.join(dest_day, 'input.txt')

    with open(input_path, 'w', encoding='utf-8') as input_file:
        response = requests.get(f'{day_url}/input', cookies={'session': session}, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        input_data = soup.get_text(strip=True)
        input_file.write(input_data)

    log(f'Input data for {Colors.colorize(year, Colors.BOLD)}-{Colors.colorize(day, Colors.BOLD)} collected successfully!', level="INFO")
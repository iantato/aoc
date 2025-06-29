import argparse
from utils import collect_aoc_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code utility.")
    parser.add_argument('-d', '--day', type=str, required=True, help="Day of the Advent of Code challenge (e.g., '1').")
    parser.add_argument('-y', '--year', type=str, required=True, help="Year of the Advent of Code challenge (e.g., '2024').")
    parser.add_argument('--collect', action='store_true', help="Collect input and description for the specified day.")

    args = parser.parse_args()

    if args.collect:
        collect_aoc_data(args.day, args.year)
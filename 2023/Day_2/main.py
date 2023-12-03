import re
from typing import Dict

def get_input_data(file_path: str) -> list:
    with open(file_path, 'r') as f:
        text = f.read()
    return text.split('\n')

def parse_game_data(text_input: str):
    regex = r"Game \d+: "
    text_input_without_game = re.sub(regex, '', text_input)
    return text_input_without_game

def check_cubes(color: str, number_of_dices: int, max_cubes: Dict[str, int]) -> bool:
    if number_of_dices > max_cubes[color]:
        return False
    return True

def regex_matches_game(input_data_parsed):
    regex_dices = r"(\d+) (green|red|blue)"
    matches = re.finditer(regex_dices, input_data_parsed)
    return matches

def part_1(input_data_parsed: str, game_number: int, max_cubes: Dict[str, int]) -> int:
    matches = regex_matches_game(input_data_parsed)

    for match in matches:
        dices = match.groups()
        color = dices[1]
        number_of_dices = int(dices[0])
        if not check_cubes(color, number_of_dices, max_cubes):
            return 0

    return game_number

def part_2(input_data_parsed: str, max_cubes: Dict[str, int]) -> int:
    max_values = {color: 0 for color in max_cubes.keys()}

    matches = regex_matches_game(input_data_parsed)

    for match in matches:
        dices = match.groups()
        color = dices[1]
        number_of_dices = int(dices[0])
        if number_of_dices > max_values[color]:
            max_values[color] = number_of_dices
        
    return max_values["red"] * max_values["blue"] * max_values["green"]


if __name__ == "__main__":
    games = get_input_data("2023/Day_2/input/input_1.txt")
    max_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    overall_sum = 0
    for game_num, game in enumerate(games, start=1):
        parsed_game = parse_game_data(game)
        overall_sum += part_1(parsed_game, game_num, max_cubes)
    print(f"Part 1 answer is: {overall_sum}")

    sum_of_powers = 0
    for game in games:
        parsed_game = parse_game_data(game)
        sum_of_powers += part_2(parsed_game, max_cubes)
    print(f"Part 2 answer is: {sum_of_powers}")

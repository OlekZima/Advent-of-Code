def convert_string(sequence: str) -> str:
    digits = {"one": '1',
              "two": '2',
              "three": '3',
              "four": '4',
              "five": '5',
              "six": '6',
              "seven": '7',
              "eight": '8',
              "nine": '9'
              }

    converted_sequence = ''
    tmp = ''
    converted_digit = ''
    last_char = ''
    for char in sequence:
        if converted_digit.isdigit():
            converted_sequence += converted_digit
            tmp += last_char
            converted_digit = ''
        if char.isalpha():
            tmp += char
        elif char.isdigit():
            converted_sequence += char
        for key in digits.keys():
            if key not in tmp:
                continue
            converted_digit += digits.get(key)
            tmp = ''
        last_char = char

    return converted_sequence


def part_2(file_name: str):
    with open(file_name, 'r') as f:
        sum_of_all = 0
        for line in f:
            line = convert_string(line)
            sum_of_all += 10 * int(line[0]) + int(line[-1])
    return sum_of_all


def part_1(file_name: str) -> int:
    with open(file_name, "r") as f:
        sum_of_all = 0
        for line in f:
            digits_from_line = ''
            for character in line:
                if not character.isdigit():
                    continue
                digits_from_line += character
            two_digit_number = 10 * int(digits_from_line[0]) + int(digits_from_line[-1])
            sum_of_all += two_digit_number
        return sum_of_all


print(f"Part 1 answer is: {part_1('2023/Day_1/input.txt')}")
print(f"Part 2 answer is: {part_2('2023/Day_1/input.txt')}")

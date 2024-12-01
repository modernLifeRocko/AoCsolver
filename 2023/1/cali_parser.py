calibration_document = 'input.txt'


def get_first_digit(line: str) -> int:
    for char in line:
        if char.isnumeric():
            return int(char)


def get_last_digit(line: str) -> int:
    for char in reversed(line):
        if char.isnumeric():
            return int(char)


with open(calibration_document, 'r') as docu:
    lines = docu.readlines()
    calibration_numbers = []
    for line in lines:
        first_digit = get_first_digit(line)
        last_digit = get_last_digit(line)
        calibration_numbers = [*calibration_numbers, first_digit*10 + last_digit]

    total_calibration = sum(calibration_numbers)
    print(total_calibration)

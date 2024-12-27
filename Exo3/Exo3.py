data = open('C:\\Users\\AbdelBadi\\Desktop\\Avent_Calendar\\Avent_Calendar\\Exo3\\3.txt').read()

import re

def extract_and_calculate(data):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    matches = re.findall(pattern, data)

    total = 0
    for match in matches:
        x, y = map(int, match)  # Convertir les chaînes en entiers
        total += x * y

    return total


result = extract_and_calculate(data)
print(result)
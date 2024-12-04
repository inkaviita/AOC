import re

f = "mul.txt"

with open (f) as file:
    lines = file.read()
    file.close()

pattern = r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'

muls = re.findall(pattern, lines)

sum = 0

correct = []

do = True

for mul in muls:
    if mul == "don't()":
        do = False
    elif mul == "do()":
        do = True
    else:
        if do:
            correct.append(mul)

print(correct)


def mul(m):
    numbers = re.findall(r'\d+,\d+', m)
    n = numbers[0].split(',')
    m1 = int(n[0])
    m2 = int(n[1])
    result = m1 * m2
    return result

for m in correct:
    sum += mul(m)

print(sum)


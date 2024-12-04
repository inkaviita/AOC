f = 'nuclear.txt'

with open (f) as file:
    lines = file.readlines()
    file.close()

safe_count = 0


def safety_check(line):
    data = [int(x) for x in line]
    s = sorted(data)
    sr = sorted(data, reverse=True)

    safe = True

    if (data != s and data != sr):
        safe = False

    for i in range(len(data) - 1):
        if abs(data[i] - data[i + 1]) > 3 or data[i] == data[i + 1]: 
            safe = False
    

    return safe

def damp_try(line):

    for i in range(len(line)):
        d_new = line[:]
        d_new.pop(i)
        if safety_check(d_new):
            print(line, " Passed second safety check when ", line[i], " was removed")
            return True
    return False

for line in lines:
    parsed = line.split()
    if safety_check(parsed):
        safe_count += 1
    elif damp_try(parsed):
        safe_count += 1

print("Safe count: ", safe_count)


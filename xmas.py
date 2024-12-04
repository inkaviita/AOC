f = 'xmas.txt'

with open(f) as file:
    lines = [line.strip() for line in file]  # Remove newline characters

horizontal = lines
vertical = ['' for _ in range(len(lines[0]))]  
diag_l = {}
diag_r = {}  

for i in range(len(lines)):
    for j in range(len(lines[i])):
        vertical[j] += lines[i][j]

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if i + j not in diag_l:
            diag_l[i + j] = ''
        diag_l[i + j] += lines[i][j]

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if i - j not in diag_r:
            diag_r[i - j] = ''
        diag_r[i - j] += lines[i][j]

diag_l = list(diag_l.values())
diag_r = list(diag_r.values())

def generate_words(input_string, word_length):
    if len(input_string) >= word_length:
        return [input_string[i:i + word_length] for i in range(len(input_string) - word_length + 1)]

word_length = 4
vertical_words = [generate_words(col, word_length) for col in vertical]
horizontal_words = [generate_words(col, word_length) for col in horizontal]
diag_l_words = [generate_words(col, word_length) for col in diag_l]
diag_r_words = [generate_words(col, word_length) for col in diag_r]

dl_edit = [x for x in diag_l_words if x is not None]
dr_edit = [x for x in diag_r_words if x is not None]

v = [item for sublist in vertical_words for item in sublist]
h = [item for sublist in horizontal_words for item in sublist]
dl = [item for sublist in dl_edit for item in sublist]
dr = [item for sublist in dr_edit for item in sublist]

all = v + h + dl + dr

xmas_count = 0

for item in all:
    if item == "XMAS" or item == "SAMX":
        xmas_count += 1


x_count = 0

for i in range(len(lines) - 2):
    for j in range(len(lines[0]) - 2):

        diag1 = lines[i][j] + lines[i + 1][j + 1] + lines[i + 2][j + 2]
        diag2 = lines[i][j + 2] + lines[i + 1][j + 1] + lines[i + 2][j]

        if ((diag1 == "SAM" or diag1 == "MAS") and (diag2 == "SAM" or diag2 == "MAS")):
            x_count += 1

print("XMAS count: ", xmas_count)
print("X count: ", x_count)
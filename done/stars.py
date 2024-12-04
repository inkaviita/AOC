
f = "star.txt"

with open (f) as file:
    lines = file.readlines()
    file.close()

left = []
right = []

for x in lines:
    in_parts = x.split()
    left.append(int(in_parts[0]))
    right.append(int(in_parts[1]))

l = sorted(left)
r = sorted(right)

sum = 0
sim = 0

#sum
for i in range(len(l)):
    sum += abs(l[i] - r[i])

#sim
for i in range(len(l)):
    sim += l.count(r[i])*r[i]


print("Total sum of IDs: ", sum)
print("Similarity: ", sim)



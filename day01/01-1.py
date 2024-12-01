# Advent of Code Day 1

# Step 1 - read in file
with open ('./cases/set2', 'r') as casefile:
    lines = casefile.read().splitlines()

# Step 2 - Split into two lists

set1 = []
set2 = []

for line in lines:
    var = line.split("   ")
    set1.append(var[0])
    set2.append(var[1])

set1.sort()
set2.sort()


distances = []

counter = 0
while (counter < len(set1)):
    distances.append(abs(int(set1[counter]) -  int(set2[counter])))
    counter = counter + 1

sumDistances = 0
for val in distances:
    print(val)
    sumDistances = sumDistances + val

print('sum: ' + str(sumDistances))
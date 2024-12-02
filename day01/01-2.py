# Advent of Code Day 1 - Part 2

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


# Step 3 - Count instances from 1st list in 2nd list
instanceCount = []

counter = 0
while (counter < len(set1)):
    instances = 0
    for line in set2:
        if (line == set1[counter]):
            instances += 1
    instanceCount.append(instances)
    counter += 1


#Step 4 - Calculate Similarity Scores
sumSimilarity = 0
print(len(set1))
counter = 0
while (counter < len(set1)):
    similarityScore = (int(set1[counter]) * instanceCount[counter])
    sumSimilarity += similarityScore
    counter += 1


print('sum similarityScore: ' + str(sumSimilarity))
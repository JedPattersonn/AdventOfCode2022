#THis is the solution to part 2, I have not got part 1 saved :()

with open('day1.txt') as topo_file:
    score = 0
    total = 0
    totalList = []
    for line in topo_file:
        if line == "\n":   
            totalList.append(score)
            score = 0
        else:
            score = score + int(line)   
totalList.sort()
for i in totalList[-3:]:
    total = total + i
print(total)

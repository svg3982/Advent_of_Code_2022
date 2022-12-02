ip =  open('dec1_input.txt')
elves = []
elf = []
for line in ip:
    if line == '\n': #line break for new elf
        elves.append(elf)
        elf = []
        continue
    new_line = line.replace("\n", "")
    elf.append(int(new_line))
elves.append(elf) #make sure to append final elf in input
ip.close()

print("number of elves",len(elves))
print(max([sum(x) for x in elves]))

#part2
max3 = sorted([sum(x) for x in elves], reverse=True)[:3]
print(sum(max3))
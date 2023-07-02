elf_cal=[]

with open("input.txt") as data:
    elf_cal = data.read().split('\n\n')
    # print (elf_cal)
for index, elf in enumerate(elf_cal):
        calories = elf.split('\n')
        total = 0
        for calorie in calories:
            if calorie != '':
                print (calorie)
                total += int(calorie)
        elf_cal[index] = total

        # print(elf_cal)

print (max(elf_cal))

top3_elfs = sum(top for top in sorted(elf_cal, reverse=True)[:3])

print(sorted(elf_cal, reverse=True)[:3])
print(top3_elfs)

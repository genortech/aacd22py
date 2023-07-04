item = []
charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
chars = list(charset)
nums = [str(i) for i in range(1,53)]
orddict = dict(zip(chars,nums))
# print(orddict)
output = 0
with open("input.txt") as data:
    rucksacks = data.read().split('\n')

    print(rucksacks[0:3])
    for rucksack in rucksacks:
        compart1, compart2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]

        a_set = set(compart1)
        b_set = set(compart2)
        # print("A ",a_set)
        # print("B ",b_set)
        # print("1 ",compart1)
        # print("2 ",compart2)
        common_item = a_set.intersection(b_set)
        # print(common_item)
        for i in common_item:
            item.append(i)
        # print(item)

    # print(item)
    for i in range(len(item)):
            if item[i] in chars:
               # print(item[i])
               # print(orddict[item[i]])
               output += int(orddict[item[i]])

    print(output)
    #Part 2

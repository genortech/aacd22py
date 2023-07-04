item = []
item2 = []
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
chars = list(charset)
nums = [str(i) for i in range(1, 53)]
orddict = dict(zip(chars, nums))
# print(orddict)
output = 0
output2 = 0
with open("input.txt") as data:
    rucksacks = data.read().split("\n")

    # print(rucksacks[0:3])
    for rucksack in rucksacks:
        compart1, compart2 = (
            rucksack[: len(rucksack) // 2],
            rucksack[len(rucksack) // 2 :],
        )

        a_set = set(compart1)
        b_set = set(compart2)
        #     # print("A ",a_set)
        #     # print("B ",b_set)
        #     # print("1 ",compart1)
        #     # print("2 ",compart2)
        common_item = a_set.intersection(b_set)
        #     # print(common_item)
        item.extend(iter(common_item))
    #         # print(item)

    # # print(item)
    for item_ in item:
        if item_ in chars:
            # print(item[i])
            # print(orddict[item[i]])
            output += int(orddict[item_])
    # print(output)
    # Part 2
    # for i in range(len(rucksacks)):
    # # print (rucksacks[i])
    # rucksack1 = rucksacks[i]
    # rucksack2 = rucksacks[i+1]
    # rucksack3 = rucksacks[i+2]
    #
    # print("R",i, rucksack1)
    # print("R",i+1, rucksack2)
    # print("R",i+2, rucksack3)
    # i += 3
    k = 3
    for j in range(0, len(rucksacks)-1,3):
        grouped_sacks = rucksacks[j:k]
        print (grouped_sacks)
        c_set = set(grouped_sacks[0])
        d_set = set(grouped_sacks[1])
        e_set = set(grouped_sacks[2])

        common_item2 = c_set.intersection(d_set,e_set)
        print ("CommonItem", common_item2)
        item2.extend(iter(common_item2))
        k +=3

    for item2_ in item2:
        if item2_ in chars:
            output2 += int(orddict[item2_])

    print(output2)

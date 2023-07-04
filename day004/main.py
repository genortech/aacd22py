
with open("input.txt", 'r') as data:
    pairs = data.read().split("\n")

pairs = 0
for section in pairs:
    section1, section2 = section.split(',')
    print(section1, section2)

    section1 = [int(i) for i in section1.split('-')]
    section2 = [int(i) for i in section2.split('-')]

    print(section1, section2)








#first attempt tested
# test_pairs = pairs[0:3]
    # for test_pair_ in test_pairs:
    #     print(test_pair_)
    #     pair = test_pair_.split(",")
    #     print(pair)
    #     for pair_ in pair:
    #         sections = pair_.split("-")
    #         print(sections)
    #         item.extend(iter(sections))]
    #         print("item",item)

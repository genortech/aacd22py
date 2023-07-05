
with open("input.txt", 'r') as data:
    pairs = data.read().strip().split("\n")

count = 0
count1 = 0
for section in pairs:
    print(section)
    section1, section2 = section.split(',')
    # print(section1, section2)

    section1 = [int(i) for i in section1.split('-')]
    section2 = [int(i) for i in section2.split('-')]

    print('sect1', section1,'sect2', section2)

    if section1[0] <= section2[0] and section1[1] >= section2[1]:
        count +=1
    elif section1[0] >= section2[0] and section1[1] <= section2[1]:
        count+=1

    print (count)

# Part two

    if section1[0] <= section2[1] and section2[0] <= section1[1]:
        count1 +=1


    print(count1)

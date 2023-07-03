player_one = []
player_two = []
player_one_score  = 0
player_two_score = 0

#A rock
#B paper
#C scissors

#Y rock 1pt
#X paper 2pt
#Z scissors 3pl

#win 6pt
#draw 3pt
#loose 0pt

with open("input.txt", 'r') as data:

    while 1:

        char = data.read(1)
        if not char:
            break

        if char in ('A','B','C'):
            player_one.append(char)
        elif char in ('X','Y','Z'):
            player_two.append(char)


# print ("player one", player_one)
# print ("player two", player_two)

    for item , item1 in zip(player_one, player_two):
        # print(f'Item 1: {item}', f'Item 2: {item1}')

        if item == 'A' and item1 =='X':
            player_two_score += 1 + 3
        if item == 'A' and item1 =='Y':
            player_two_score += 2 + 6
        if item == 'A' and item1 =='Z':
            player_two_score += 3
        if item == 'B' and item1 =='X':
            player_two_score += 1
        if item == 'B' and item1 =='Y':
            player_two_score += 2 + 3
        if item == 'B' and item1 =='Z':
            player_two_score += 3 + 6
        if item == 'C' and item1 =='X':
            player_two_score += 1 + 6
        if item == 'C' and item1 =='Y':
            player_two_score += 2
        if item == 'C' and item1 =='Z':
            player_two_score += 3 + 3

    print("player two score", player_two_score)

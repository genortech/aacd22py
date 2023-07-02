player_one = []
player_two = []

with open("input.txt", 'r') as data:

    while 1:

        char = data.read(1)
        if not char:
            break
        print ("data 2" , char)

        if char in ('A','B','C'):
            player_one.append(char)
        elif char in ('X','Y','Z'):
            player_two.append(char)


print ("player one", player_one)
print ("player two", player_two)

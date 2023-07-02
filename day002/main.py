player_one = []
player_two = []

with open("input.txt") as data:
    # print (data.read(1))
    while True:
        if data.read(1) == 'A' or 'B' or 'C':
            player_one = data.read(1)
        elif data.read(1) == 'X' or 'Y' or 'Z':
            playeer_two = data.read(1)
        elif not data.read(1):
            break
    print ("player one", player_one)
    print ("player two", player_two)

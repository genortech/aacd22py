f = open("input.txt", "r")

# print (f)
# print (f.read())
data = f.read().splitlines()
# print (data)
# PART ONE
maximum = 0
maximum2 = 0
maximum3 = 0
count = 0
for calorie in data:
    if calorie == "":
        count = 0
    else:
        count += int(calorie)

    if count > maximum:
        maximum3 = maximum2
        maximum2 = maximum
        maximum = count

    # PART TWO
    elif count > maximum2:
        maximum3 = maximum2
        maximum2 = count
    elif count > maximum3:
        maximum3 = count


print(maximum)
print(maximum2)
print(maximum3)

print(maximum + maximum2 + maximum3)

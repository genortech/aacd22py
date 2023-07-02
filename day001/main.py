f = open('input.txt', 'r')

# print (f)
# print (f.read())
data = f.read().splitlines()
# print (data)
# PART ONE
max = 0
max2 = 0
max3 = 0
count = 0
for calorie in data:
    if calorie == '':
        count = 0
    else:
        count += int(calorie)

    if count > max:
        max = count
    #PART TWO
    elif count > max2:
        max2 = count
    elif count > max3:
        max3 = count


print (max)
print (max2)
print (max3)

print (max+max2+max3)

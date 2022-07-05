#1 Basic
for index in range(151):
    print(index)
#2 Multiples of five
for index in range(5, 1001, 5):
    print(index)
#3 counting, the Dojo Way
for index in range(1, 101):
    if index % 5 == 0:
        if index % 10 == 0:
            print("Coding Dojo")
        else:
            print("Coding")
    else:
        print(index)
#4 Whoa. That Sucker's huge
sum = 0
for index in range(1, 500000, 2):
    sum = sum + index
print(sum)
#5 countdown by Fours
for index in range(2018, 0, -4):
    print(index)
#6 flexible counter
lownum = 5
highnum = 20
mult = 4
for index in range(lownum, highnum + 1):
    if index % mult == 0:
        print(index)
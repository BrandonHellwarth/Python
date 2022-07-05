# print(type(24))
# print(type(3.9))
# print(type(3j))
# no need for ;
# - - - - - - - - - - - - - - - - - - - - - - - - -
first_name = "Brandon"#an empty string is a flase value, a string with content is a true value
last_name = "Hellwarth"
age = 23
# print("Hi my name is Tyler and I am 23 years old...I think.")
# what if we wanted dynamic variables?
# print("Hi my name is %s %s and I am %d years old...I think" % (first_name, last_name, age))
#Then switched too...
# print("Hi my name is {} {} and I am {}years old...I think.".format(first_name, last_name, age))
#and is now currently...
print(f"Hi my name is {first_name} {last_name} and I am {age} years old...I think.")#The f before the string means format
y = "2"
# print(y + 5)python can't combine strings and ints like JS
if first_name:#will print yes if first_name has a value of true
    print("yes")
else:
    print("no")
# - - - - - - - - - - - - - - - - - - - - - - - -
            #  0         1       2
brothers = ['tyler', 'curtis', 'joe', 'bob']
# brothers[1] = "bob" .push is .append in python
brothers.append("bob")
print(brothers)
person = {
    'first_name' : 'Brandon',
    'last_name' : 'Hellwarth',
    'age' : 23,
    'first_name1' : 'Jim',
    'last_name1' : 'Hellwarth',
    'age1' : 23,
    'first_name2' : 'John',
    'last_name2' : 'Hellwarth',
    'age2' : 23
    }
print(person['first_name'])#result is Jim
#- - - - - - - - - - - - - - - - - - - - - - - - - -
for brother in brothers:
    print(brother)
#A FUNCTION IS WHAT IT RETURNS
# for index in range(1, len(brothers), 2):
#     brother = brothers2[index]
#     print(brother)
for index in range(0, 101, 2):
    print(index)#This will print all even numbers between 0 and 100
i=0
while(i < len(brothers)):
    if i % 3 == 0:
        print(brothers)
    i += 1#no i++ in python. Without this statement, this loop will run forever.
# - - - - - - - - - - - - - - - - - - - - - - - - - -
import random #need this to use random.randint, needs a start and end
def randomize_list(new_list):
    return_list = []
    for item in new_list:
        random_num = random.randint(0, len(new_list) - 1)
        item = new_list[random_num]
        return_list.append(item)
    return return_list
print(randomize_list(brothers))#randomizes brothers

def run_times(num, new_list):
    for index in range(num):
        print(randomize_list(new_list))
print(run_times(5, brothers))#returns none because no return statement

def add(num1, num2):
    return num1 + num2
print(add(5, 5))
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
#1
x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30
#2
def iterateDictionary(some_list):
    for index in range(len(some_list)):
        print("first_name - " + some_list[index]['first_name'] + ", last_name - " + some_list[index]['last_name'])

students1 = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

iterateDictionary(students1)
#3
def iterateDictionary2(key_name, some_list):
    for index in range(len(some_list)):
        print(some_list[index][key_name])

iterateDictionary2('first_name', students1)
iterateDictionary2('last_name', students1)
#4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printinfo(some_dict):
    keys = list(some_dict.keys())#stores keys in a list
    for index in range(len(some_dict)):#runs for each key in the dictionary
        key = len(some_dict[keys[index]])
        print(f"{key} " + keys[index])#prints the length of the list corresponding to the dictionary key and key name
        for i in range(len(some_dict[keys[index]])):#runs for each value in the key's list
            print(some_dict[keys[index]][i])#prints each value inside of the corresponding key
printinfo(dojo)

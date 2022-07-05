# h1
## h2
### h3

# Python VS Javascript

- Data Types
    - Int, Floats
    - String
    - Bool
    - Arrays
    - Obj
    - Tuples
-Loops
-Conditionals
-Functions

## Numbers

Ints and Floats
35  -->  35.0

## String
How do we know something is a string? first_name = "Brandon"

## Bool
true and false

## Arrays -> List
```py
brothers = ['tyler', 'curtis', 'joe']
```
## Obj ->
- key - value pairs

```JS
function add(num1, num2){
    return num1 + num2;
}
add(5,7);
```
Python is indent sensitive compared to JS
```PY
def add(num1, num2):
    print('hello')
    if num1 == 5:
        print("I am 5")
    return num1 + num2

add(5,7)
```

## Tuples
Tuples cannot be changed(immutable), they are a snapshot of a data type

## Conditionals
```JS
var age = 23
if(age >= 21){
    return "You may enter";
}
else if(age >= 65){
    return "You may Enter and get a free drink!"
}
else{
    return "You shall not pass";
}
```

```PY
age = 23
if age >= 65:
    return "You may Enter and get a free drink!"
elif age >= 21:
    return "You shall not pass"
else:
    return "You shall not pass"
```
## Function
`what is a function`
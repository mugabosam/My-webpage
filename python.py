for i in range (13,2,-1):
    print(f"multiplication table of {i}")
    print("______________________________")
    for j in range(1,13):
        print(f"{i} * {j} = {i*j}")
    print()

for i in range(10,0,-1):
    print(i)
print("_____________________")


for i in range(2,11,2):
    print(i)

print("_______________________")


sum=0
for i in range(100,201):
    sum +=i
print(f"sum is {sum}")

print("_______________________")

def function():
    print("my", end=" ")
    print(" first", end=" ")
    print("program")

function()

print("__________________________")

def minimum(first,second):
    if first <second:
        print(first)
    else:
        print(second)

num1=10
num2=20

minimum(num1,num2)

print("_________________________")
class Employee:
    id=None
    salary=None
    department=None
james=Employee()
james.id=100
james.salary=3000
james.department="IT"
print(james.id)
print(james.department)
print(james.salary)

print("___________________")
class employee:
    def __init__(self,id,salary,department=None):
        self.id=id
        self.salary=salary
        self.department=department

james=employee(123,25000,"IT")
print(james.id)
print(james.salary)
print(james.department)

print("______________________")

def replace_vowels(s):
    # create a string of vowels
    vowels = "aeiouAEIOU"
    # create an empty string to store the result
    result = ""
    # loop through each character in the input string
    for char in s:
        # check if the character is a vowel
        if char in vowels:
            # replace it with '*'
            result += "*"
        else:
            # keep it as it is
            result += char
    # return the result
    return result

# example of using the function
my_string = "mi boi, will eat mi drum!"
print(replace_vowels(my_string)) 

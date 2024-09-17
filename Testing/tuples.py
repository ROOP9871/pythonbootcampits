#tuples can store the multiple data cannot change
myTuple = (" Rohit", "Rohit", "Anshu", "Anuj")
# print( myTuple)

# print(type(myTuple))

# print(myTuple[0])

# myTuple[1] = "Deepak"

# print(myTuple)

# Use a for loop to print each value
for value in myTuple:
    print(value)

#dictionary can store multiple data in key value pair

myDict = {
    "name": "Ashish tyagi"
    "contact" "985764767"
    }
# print(type(myDict))
# print( myDict)
# for keys in myDict:
#     print(myDict[item])

print(myDict.get("name"))
myDict["name"] = "Deepak"
print(myDict)

#OOPS
#CLASS AND OBJECT
#class Mohit:
# age = 22
#print("from Sahibabad")
#X = Mohit()
#print(X.age)
#from datetime import date
# from datetime import date

# class Person:
#     def __init__(self, name, birth_year):
#         self.name = name
#         self.birth_year = birth_year
    
#     def calculate_age(self):
#         current_year = date.today().year
#         return current_year - self.birth_year

# # Create a Person object
# person = Person("Roop", 2003)

# # Calculate and print the age
# age = person.calculate_age()
# print(f"{person.name} is {age} years old.")

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def is_adult(self):
#         if self.age >= 18:
#             return f"{self.name} is an adult."
#         else:
#             return f"{self.name} is not an adult."

# # Get input from the user
# name = input("Enter the person's name: ")
# age = int(input("Enter the person's age: "))

# # Create an instance of the Person class
# bornyear = int (input("Enter your bornyear"))
# currentyear = int (input("Enter your currentyear"))
# class Agecal:
#     ageInyear =  currentyear - bornyear
#     dob = "08 oct 2003"
#     age = Agecal()
#     print(age.ageInyear, age.dob)
def age(dob1):
    print(dob1)
    
    def age (dob, name):
        print()

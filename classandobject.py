from datetime import date

class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
    
    def calculate_age(self):
        current_year = date.today().year
        return current_year - self.birth_year

# Create a Person object
person = Person("Roop", 2003)

# Calculate and print the age
age = person.calculate_age()
print(f"{person.name} is {age} years old.")

#collect person details using class and object declaration,
class Person:
    # Constructor (__init__) to initialize the object
    def __init__(self, name, age):
        self.name = name  # Attribute to store the person's name
        self.age = age    # Attribute to store the person's age

    # Method to display information about the person
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Create an object (instance) of the Person class
person1 = Person("Ritu Raj", 30)

# Access the object's attributes and methods
print("Person 1 details:")
person1.display_info()

# Create another object
person2 = Person("Dolly Chadda", 25)

print("\nPerson 2 details:")
person2.display_info()

# Create another object
person3 = Person("Himanshi Guatam", 25)

print("\nPerson 3 details:")
person3.display_info()

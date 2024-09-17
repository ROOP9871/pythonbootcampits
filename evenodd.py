import datetime
x = datetime.datetime.now()
print(x.year)
#to create new file and add my name also close the file
# Name = input("Enter your name")
# CollegeName = input("Enter your  collegename")
# Email = input("Enter your Email")
# data = Name + Email + CollegeName
f = open("roop.txt", "w")
f.write(" data")
f.close()
f = open("roop.txt", "r")
print(f.read(4))
i = 1
# while i < 21:
#   print(i)
#   break
#   i += 1
#   i
# while i < 21:
#   i += 1
#   print(i)
#   continue
from datetime import datetime
#get the birthdate input from the user in yyyy-mm-dd format
birthdate_str = input("Enter your birthdate ( yyyy-mm-dd):")

#convert the input string to a datetime object
birthdate = datetime.strptime(birthdate_str, "%y-%m-%d")
today = datetime.today()

day_alive = (today - birthdate).days

print(f"you have been alive for {day_alive} days.")


import json

# Get input from the user
name = input("Enter your name: ")
collegename = input("Enter your college name:")
age = int(input("Enter your age: "))
fee = int(input("Enter your fee: "))
birthdate = input("Enter your birthdate (YYYY-MM-DD): ")

# Create a dictionary with the input data
user_data = {
    "name": name,
    "collegename": collegename,
    "age": age,
    "fee": fee,
    "birthdate": birthdate
}

# Specify the filename
filename = "user_data.json"

# Write the data to a JSON file
with open(filename, 'w') as file:
    json.dump(user_data, file, indent=4)

print(f"Data saved to {filename}")

import csv

# Define the data you want to write to the CSV file
data = [
    ["Name", "Age", "City","Email","Contact"],
    ["Roop", 22, "Sahibabd","roopk8366@gmail.com","9667790198"],
    ["Rohit", 23, "Village Sahibabad","chancha653@gmail.com","9987700198"],
    ["Mohit", 23, "Mohan Nagar","rohitbca2021@gmail.com","9669807098"]
]

# Specify the filename
filename = 'example.csv'

# Open the file in write mode and create a CSV writer object
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the data to the CSV file
    writer.writerows(data)

print(f"Data has been written to {filename}")



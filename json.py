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




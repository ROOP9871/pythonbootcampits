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

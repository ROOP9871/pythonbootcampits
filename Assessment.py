# # YEAR CALCULATION BY USER INPUT
# currentyear = int(input('Enter the currentyear'))
# bornyear = int(input('Enter the bornyear'))
# ageInyear = currentyear - bornyear
# print( "my age",ageInyear)


# #currency converted into dollars to rupees
# print("convert dollars into rupees")
# dollarsamount = int(input("Enter the amount in doll."))
# dollIntorupees = (dollarsamount * 84)
# print(dollarsamount, "convert into rupees" , dollIntorupees)

def calculate_bmi(weight, height):
    try:
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return "Height cannot be zero."

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Taking user input for weight and height
try:
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    
    if isinstance(bmi, str):
        print(bmi)  # Error case
    else:
        category = bmi_category(bmi)
        print(f"Your BMI is: {bmi}")
        print(f"You are categorized as: {category}")
except ValueError:
    print("Please enter valid numbers for weight and height.")

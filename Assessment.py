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


#BMI calculator
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

print(f"Your BMI is: {bmi}")
print(f"You are categorized as: {category}")

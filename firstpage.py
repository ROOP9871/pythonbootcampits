print("Roop kishore")
a = 10
b = 37
sum = a + b
print(sum)
sub = b - a
print(sub)
product = a * b
print(product)
divide = b / a
print(divide)
# num1 = 2.39
# num2 = 334
# num3 = 'Rohit'

# print(type(num1))
# print(type(num2))
# print(type(num3))
#YEAR CALCULATION BY USER INPUT
# currentyear = int(input('Enter the currentyear'))
# bornyear = int(input('Enter the bornyear'))
# ageInyear = currentyear - bornyear
# print( ageInyear)

# # wrp to convert currency
# # print("convert rupees into dollars")

# rupeesamount = int(input("Enter the amount in Rs."))
# rsIndollars = (rupeesamount / 84)
# print(rupeesamount, "convert into dollar" , rsIndollars)


# # print("convert dollars into rupees")
# dollarsamount = int(input("Enter the amount in doll."))
# dollIntorupees = (dollarsamount * 84)
# print(dollarsamount, "convert into rupees" , dollIntorupees)


# # wap to check the your are eligible for voting or not
# # for voting you must greater than 17
# userage = int(input('Enter your age'))


# if( userage > 18):
#    print('your are eligible for voting')
    
# else:
#     print('you are not eligible for voting')
    
    
# # if   gender is female and your age above 18
# # if   gender is male then they can apply for private job

# gender = input("Enter your gender")
# age = int(input('Enter your age'))

# if (gender == 'male' and age > 17):

#    print('you are eligible for private job')
# elif(gender == 'female' and age > 17):
#    print('you are eligible for government job')
# else:
#    print('you are  not eligible for any job')
#     method 2
#     if (age > 17):
#        if(gender == "female"):
#            print("you are eligible for government job'")
#        elif(gender == 'male'):
#            print('you are eligible for private job')
#             wap three number greatest number
# num1 = int(input('enter num1'))
# num2 = int(input('enter num2'))
# num3 = int(input('enter num3'))
# if(num1 > num2 and num1 > num3):
#     print('num1 is largest')
# elif(num2 > num1 and num2 > num3):
#     print('num2 is largest')
# else:
#     print('num3 is largest')

#switch condition is replacement of multiple if else case/block
friendname = ["Roop", "Kishore", "Rohit", 1,2,3,4,5, 1]
print(friendname)
print("before", friendname)
#to add new name in list
friendname.append("Rohit Kumar")
print('after', friendname)
friendname.insert(0,"Mohit")
friendname.insert(3,"Mohit")
# print after adding new name
print("add name at index 0", friendname)
friendname.remove("Mohit")
print( friendname)
friendname.pop(3)
print(friendname)
#to print element in the given list
# for names in  friendname:
#square root
# p = 9
# p_sqrt = p ** 0.5
# print('the square of %0.2f is %0.2f'%(p ,p_sqrt))

# #formate value( 'the value of f is {} and k is {}'.format(f,k))
# f = 56
# k = 45
# print ('the value of f is {} and k is 0{}'.format(f,k))

# # using input  to take input

# value = input('Enter a value: ')

# print('you Entered:' , value)
# print('Data type of value:', type(value))

# 1 to 10 print
from datetime import datetime

# Replace this with your birthdate (year, month, day)
birthdate = datetime(2003, 10, 8)

# Get today's date
today = datetime.today()

# Calculate the difference in days
days_alive = (today - birthdate).days

# Print the result
print(f"You have been alive for {days_alive} days.")




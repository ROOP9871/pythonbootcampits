# if(user age > 18):

#     print('your are eligible for voting')
# else:
#     print('you are not eligible for voting')
# # if   gender is female and your age above 18
# # if   gender is male then they can apply for private job

gender = input("Enter your gender")
age = int(input('Enter your age'))

if (gender == 'male' and age > 17):

   print('you are eligible for private job')
elif(gender == 'female' and age > 17):
   print('you are eligible for government job')
else:
   print('you are  not eligible for any job')
#     method 2
#     if (age > 17):
#        if(gender == "female"):
#            print("you are eligible for government job'")
#        elif(gender == 'male'):
#            print('you are eligible for private job')
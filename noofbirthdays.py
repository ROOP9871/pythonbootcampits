from datetime import datetime
#get the birthdate input from the user in yyyy-mm-dd format
birthdate_str = input("Enter your birthdate ( yyyy-mm-dd):")

#convert the input string to a datetime object
birthdate = datetime.strptime(birthdate_str, "%y-%m-%d")
today = datetime.today()

day_alive = (today - birthdate).days

print(f"you have been alive for {day_alive} days.")
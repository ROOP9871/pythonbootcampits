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
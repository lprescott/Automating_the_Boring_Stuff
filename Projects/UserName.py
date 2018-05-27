#This program accepts a first, middle and last name -- suggesting user names based therof.

firstName = "" 
middleName = "" 
lastName = ""

print("Please enter your first name:")
firstName = input()

print("Please enter your middle name:")
middleName = input()

print("Please enter your last name:")
lastName = input()

print("Your name:")
print(firstName, middleName, lastName)
print(firstName, lastName)
print(firstName[0] + '.', lastName)
print(firstName[0] + '.', middleName[0] + '.', lastName)

print("\nYour username:")
print(firstName + middleName + lastName)
print(firstName.lower() + lastName)
print(firstName[0].lower() + lastName)
print(firstName[0].lower() + middleName[0].lower() + lastName)
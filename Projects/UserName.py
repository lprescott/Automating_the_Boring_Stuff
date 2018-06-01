#! python3
#This program accepts a first, middle and last name -- suggesting user names based therof.

firstName = "" 
middleName = "" 
lastName = ""

firstName = input("Please enter your first name:")
middleName = input("Please enter your middle name:")
lastName = input("Please enter your last name:")

print("\nYour name:")
print(firstName, middleName, lastName)

print("\nYour usernames:")
print(firstName + middleName + lastName)
print(firstName.lower() + middleName.lower() + lastName.lower())
print(firstName + lastName)
print(firstName.lower() + lastName)
print(firstName[0] + lastName)
print(firstName[0].lower() + lastName)
print(firstName[0], middleName[0], lastName[0], sep='')
print(firstName[0].lower(), middleName[0].lower(), lastName[0].lower(), sep='')

input("\nPress Enter to exit...")
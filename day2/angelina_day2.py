'''
Date: 13/11/2024
Author: Angelina Rose Varghese
Description: To verify whether the password given by user is strong or not
'''
password=str(input("Enter password: "))
length=len(password)
if length>7:
    print ("Password is strong")
else:
    print("password is weak")



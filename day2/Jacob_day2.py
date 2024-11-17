'''
Author:Jacob Thomas
Date:17/11/24
Description:Write a program that generates a random password of a user-specified length
'''
password=input("Enter your password: ")
lenght_password = len(password)
if lenght_password>7:
    print("Password is strong")
else:
    print("Password is weak")
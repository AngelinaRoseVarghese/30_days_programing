'''Create a program for Basic Password Generator
Write a program that generates a random password of a user-specified length.
If password is greater than 7 characters ; password is strong.
If password is less than 7 characters password is weak'''
password=str(input("Enter the password:"))
length=len(password)
if length>7:
    print("password is strong")
else:
     print("Password is weak")
'''
Author: Jacob Thomas
Date: 17/11/2024
Description: Display the multiplication table for a user-input number.
'''
num=int(input("Enter the number"))
for i in range(1,15):
    multiplication=num*i
    print(multiplication)
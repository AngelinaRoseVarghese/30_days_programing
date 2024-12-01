'''
Author:Jacob Thomas
Date:01/12/2024
Description:Write a function check_even_odd that takes an integer as input and returns whether the number is "Even" or "Odd".
'''
def check_even_odd(num):
    if num %2 ==0:
        print("Even Number")
    else:
        print("Odd Number")
num=int(input("Enter the number: "))
check_even_odd(num)
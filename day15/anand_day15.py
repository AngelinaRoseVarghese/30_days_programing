'''author:Anand Krishna M A
description:Write a function check_even_odd that takes an integer as input and returns whether the number is "Even" or "Odd"
Date:29/11/2024'''


def even_odd(x):
    if x%2==0:
        print("Even")
    else:
        print("odd")
while True:
    num=int(input("Enter a number:"))
    even_odd(num)
    a=input("Do you want to check another no:(Y/N)")
    if a in'nN':
        break
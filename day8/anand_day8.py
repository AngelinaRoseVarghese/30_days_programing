'''author:AnandKrishna M A
description:Write a program to check whether the given year is a leap year or not using if-else'''
year=int(input("Enter the year:"))
if year%4 == 0:
    print(f"{year} is a leap year.")
else:
    print("it is not a leap year")
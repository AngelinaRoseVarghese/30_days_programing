'''
Author:Jacob thomas
Date:18/11/2024
Description:Write a program to check whether the given year is a leap year or not using if-else.
'''
year=int(input("Enter the year"))
if year%4==0:
    print("The given year",year,"is a leap year")
else:
    print('The given year', year ,' is not a leap year')
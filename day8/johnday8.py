'''
Author:John Kuriakose
Description: A program use to check leap year using if-else
 to check if a given year is a leap year.
'''
year=int(input("Enter the year: "))
if year%4==0 and (year%100!=0 or year%400==0):
    print(year,"is a leap year")

else:
    print(year, "is not a leap year")


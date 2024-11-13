'''
date: 13/11/2024
Author: Angelina Rose Varghese
Description:  a program that takes two numbers (start and end) from the user and calculates the sum of all integers between those numbers using a for loop.
'''

start=int(input("Enter a beginning number: "))
end=int(input("Enter a ending number: "))
result=0
for i in range(start,end+1):
    result=result+i
    print(result,",", end=" ")




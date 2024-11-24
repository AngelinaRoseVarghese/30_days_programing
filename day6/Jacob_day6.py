'''
Author: Jacob Thomas
Date: 17/11/2024
Description: Write a program that takes two numbers (start and end) from the user and calculates the sum of all integers between those numbers using a for loop.
'''
'''
num1=int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
result = 0
for i in range(num1,num2+1):
    result=result+i
    print("result",result)
    '''

start=int(input("Enter a beginning number: "))
end=int(input("Enter a ending number: "))
result=0
for i in range(start,end+1):
    result=result+i
    print(result,",", end=" ")
print(f"The sum of all integers between {start} and {end} is: {result}")






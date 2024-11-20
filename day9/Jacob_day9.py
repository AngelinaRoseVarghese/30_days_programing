'''
Author:Jacob Thomas
Date:20/11/2024
Description:Write a program that finds the largest and smallest numbers in a list using for loops and if statements.
'''
numbers=[15,88,45,78,32,54]
largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("The largest number is :",largest)
print('The smallest number is :',smallest)




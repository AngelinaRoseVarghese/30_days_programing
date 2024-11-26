'''
Author:Jacob Thomas
Date:22/11/2024
Description:Input a list of numbers from user and then print the squares of the number entered by the user
'''
import math

square_list=[]
num=int(input("How many numbers you want to enter: "))
for i in range(num):
    list_val=int(input("Enter the numbers to the list: "))
    square_list.append(math.sqrt(list_val))
print(square_list)




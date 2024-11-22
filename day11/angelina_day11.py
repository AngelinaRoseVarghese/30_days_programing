'''
Date: 22/11/2024
Author:Angelina Rose Varghese
Description:Input a list of numbers from user and then print the squares of the number entered by the user
'''
import math
my_list=[]
new_list=[]
num=int(input("How many numbers you want to enter: "))
for i in range(num):
    list_value=int(input("Enter the value for list: "))
    new_list.append(math.sqrt(list_value))
print (new_list)

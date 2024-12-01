'''
Author:Jacob Thomas
Date:27/11/2024
Description:Count Occurrences of an Element
Count how many times a specific element appears in a list.
python And remove the duplicate numbers from list
'''
from multiprocessing.reduction import duplicate

list=[]
num=int(input("Enter the number of elements in the list: "))
for i in range(num):
    element=int(input("Enter the numbers to the list: "))
    list.append(element)
duplicate=int(input("Enter the number to check if it has a duplicate:"))
list_1=list.count(duplicate)
print("New list",list_1)
for j in range(list_1):
    if duplicate in list:
        list.remove(duplicate)
        print("Updated list",list)
    else:
        print("None")



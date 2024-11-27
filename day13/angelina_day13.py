'''
Date:27/11/2024
Author:Angelina Rose Varghese
Description: Count Occurrences of an Element
Count how many times a specific element appears in a list.
python and remove the duplicate numbers from list
'''
list=[]
num=int(input("How many numbers you want to enter: "))
for i in range(num):
    element=int(input("Enter a number: "))
    list.append(element)
duplicate=int(input("Enter the number to check whether it has duplicate or not: "))
list1=list.count(duplicate)
print("original list",list1)
for j in range(list1):
    if duplicate in list:
        list.remove(duplicate)
        print("new list",list)
    else:
        print("none")




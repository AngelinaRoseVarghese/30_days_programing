'''
Author:Jacob Thomas
Date:25/11/2024
Description:Write a program that takes two lists as input from the user. Create a third list where:
All the even numbers from both lists appear first, sorted in ascending order.
Followed by all the odd numbers from both lists, also sorted in ascending order
'''


list1=[]
list2=[]
num=int(input("Enter the number of values to the list:"))
for i in range(num):
    list_one=int(input("Enter the values to the list: "))
    list1.append(list_one)
    print(list1)
numb=int(input("Enter the number of values in the list: "))
for j in range(numb):
    list_two=int(input("Enter the values to the list:"))
    list2.append((list_two))
    print(list2)
combined_list=list1 + list2
print(combined_list)

even_list=[]
odd_list=[]
for k in combined_list:
    if k % 2 == 0:
        even_list.append(k)
    else:
        odd_list.append(k)
    even_list.sort()
    odd_list.sort()
combined_list = even_list+ odd_list
print(combined_list)



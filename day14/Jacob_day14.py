'''
Author:Jacob Thomas
Date:01/12/2024
Desciption:Ask user to input a list and Move All Zeros to the End. Move all zeros in a list to the end, maintaining the order of non-zero elements
'''
list1=[]
num=int(input("Enter the numbers of elements in list: "))
for i in range(num):
    element=int(input("Enter the number to the list:"))
    list1.append(element)
list1.sort()
print(list1)
zero_list=[]
no_zero_list=[]
for  num in list1:
    if num==0:
        zero_list.append(num)
    else:
        no_zero_list.append(num)
updated_list=no_zero_list+zero_list
print(updated_list)
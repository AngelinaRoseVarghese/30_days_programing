'''
Date: 28/11/2024
Author: Angelina Rose Varghese
Description: Move All Zeros to the End. Move all zeros in a list to the end, maintaining the order of non-zero elements.
'''
zero=[]
non_zero=[]
num=int(input("How many number you want: "))
for i in range(num):
    num1=int(input("Enter the number including zeros: "))
    if num1==0:
        zero.append(num1)
    else:
        non_zero.append(num1)
new=non_zero+zero
print(new)







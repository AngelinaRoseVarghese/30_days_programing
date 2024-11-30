'''author:Anand Krishna M A
Description:Ask user to input a list and Move All Zeros to the End. Move all zeros in a list to the end, maintaining the order of non-zero elements
Date:28/11/2024'''


lst=eval(input("Enter the list:"))
zero_lst=[]
for i in lst:
    if i==0:
        lst.pop(lst.index(i))
        zero_lst.append(i)
print(lst+zero_lst)

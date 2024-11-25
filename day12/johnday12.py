#Author=John Kuriakose
#Description:Write a program that takes two lists as input from the user. Create a third list where:
#All the even numbers from both lists appear first, sorted in ascending order.
#Followed by all the odd numbers from both lists, also sorted in ascending order

first_list=[]
second_list=[]
num=int(input("Enter the number of values for the first list:"))
for i in range(num):
   list_one=int(input("Enter the list:"))
   first_list.append(list_one)
num=int(input("Enter the number of values for the second list"))
for j in range(num)  :
   list_two=int(input("Enter the list:"))
   second_list.append(list_two)
print("First list:",first_list)
print("Second list:",second_list)
combined_list=first_list+second_list

odd_list=[]
even_list=[]
for i in combined_list:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
    even_list.sort()
    odd_list.sort()
combined_list=even_list+odd_list
print(combined_list)
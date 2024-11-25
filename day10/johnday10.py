'''
author:John Kuriakose
description: A program based on list methods. Using index,append, insert, extend, remove, count, pop, sort, reverse, max(), min(), split.
 Ask user for the input of list.
'''
#to append elements to the list
num=int(input("Enter the number of digits in the list:"))
my_list=[]
for i in range(num):
    digits=int(input("Enter the digits:"))
    my_list.append(digits)
print(my_list)

#to find the index value of the element from the list
index_value=int(input("Enter the value of the element you want to find the location of:"))
print(my_list.index(index_value))

# to insert elements in list
insert_value=int(input("Enter the value that you want to insert:"))
insert_position=int(input("enter the position where you want to insert the value:"))
my_list.insert(insert_position,insert_value)
print(my_list)

# to extend the list
no_extend=int(input("How many numbers do you want to add to the list:"))
extend=[]
for j in range(no_extend):
    num_extend=int(input("Enter the number ypu want to extend to the list:"))
    extend=[num_extend]
    my_list.extend(extend)
print(my_list)

# to remove a variable from list
num_remove=int(input("enter the number of values you want to remove:"))
for z in range(num_remove):
    num_rem=int(input("Enter the vale you want to remove:"))
    my_list.remove(num_rem)
print(my_list)

# to count elements in the list
num_count=int(input("Enter the value you want to count:"))
print("The number of times th value", num_count ,"occurs is", my_list.count(num_count))

#to pop an element from the list
n_pop=int(input("Enter the number of values you wan to pop:"))
removed_list=[]
for y in range(n_pop):
   num_pop=int(input("Enter the index of the value you want to pop"))
   removed_list=my_list.pop(num_pop)
   print(my_list)
   print("The element popped is",removed_list)

# to sort elements in list

my_list.sort()
print ("ascending order of list is ",my_list)
my_list.sort(reverse=True)
print("descending order of list is ",my_list)

# to reverse the elements in the list
my_list.reverse()
print(my_list)

# to find maximum in the list
print(max(my_list))

# to find minimum in the list
print(min(my_list))


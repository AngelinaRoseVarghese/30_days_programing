'''
date;21/11/2024
author: Angelina Rose Varghese
description: A program based on list methods. Using index,append, insert, extend, remove, count, pop, sort, reverse, max(), min(), split.
 Ask user for the input of list.
'''
# to append elements to the list
no=int(input("How many numbers you want to enter in list : "))
my_list=[]
for i in range(no):
    num=(input("Enter a number: "))
    my_list.append(num)
print(my_list)
'''
# to find the index no from the list
location=input("Enter the  variable you want to find the position of: ")
print(my_list.index(location))

# to insert elements in list
inserting_position=int(input("Enter the position of variable you want to insert: "))
value_of_insertion=input("Enter the value you want to insert: ")
(my_list.insert(inserting_position,value_of_insertion))
print(my_list)

# to extend the list
no_extend=int(input("How many numbers you want to add to the list: "))
extend=[]
for j in range(no_extend):
    num_extend=int(input("Enter the number you want to extend to the list: "))
    extend=[num_extend]
    my_list.extend(extend)
print(my_list)

# to remove a variable from list
no_remove=int(input("How many number you want to remove: "))
for k in range(no_remove):
    remove_element = input("Enter the value of element you want to remove")
    my_list.remove(remove_element)
print(my_list)

# to count elements in the list
count_no=(input("Enter the number you want to count: "))
print("The no.of times",count_no,("is"),(my_list.count(count_no)))

# to pop a element
pop_number=int(input("Enter the index number you want to pop: "))
my_list.pop(pop_number)
print(my_list)

# to sort elements in list

my_list.sort()
print ("ascending order of list is ",(my_list))
my_list.sort(reverse=True)
print("desecnding order of list is ",(my_list))

# to reverse the elements in the list
my_list.reverse()
print(my_list)

# to find maximum in the list
print(max(my_list))
'''
# to find minimum in the list
print(min(my_list))




#





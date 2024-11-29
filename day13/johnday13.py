list=[]
num=int(input("Enter the number of elements you want to enter:"))
for i in range(num):
    values=int(input("Enter the values:"))
    list.append(values)
print("list:", list)
duplicate=int(input("Enter the value you want to check:"))
print("The numbers of times the element occur is",list.count(duplicate))
occur=list.count(duplicate)
for j in range(occur):
    if duplicate in list:
        list.remove(duplicate)
    else:
        print("None")
print("New List:",list)


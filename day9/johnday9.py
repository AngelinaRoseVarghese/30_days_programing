largest=0
smallest=10^9
Num=int(input("enter the number of numbers:"))
for i in range(Num):
    num=int(input("Enter the numbers:"))
    num_list=list([num])
    if num>largest:
        largest=num
    elif num<smallest:
        smallest=num
print(largest,"is the largest")
print(smallest,"is the smallest")

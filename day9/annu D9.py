# to find the largest and smallest in a list using loops and if statements
largest=1
smallest =1
y =int(input('how many numbers you want to enter?'))
for i in range(y):
    num=int(input('enter number'))
    list=list([num])
    if num>largest:
        largest=num
    elif num<smallest:
        smallest=num
    print("largest is",largest)
    print("smallest is",smallest)

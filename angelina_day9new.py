'''
 program finds the largest and smallest numbers in a list using for loops and if statements.
'''
largest=0
smallest=0
time=int(input("How many numbers you want to enter"))

for i in range(time):
    num = int(input("Enter digits"))
    my_list = list([num])
    if num>largest:
        largest=num

    elif smallest<num:
        smallest=num

print ("largest is",largest)
print ("smallest is",smallest)
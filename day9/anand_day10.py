'''author:Anand krishna M A
Description:program that finds the largest and smallest numbers in a list using for loops and if statements'''
lst=eval(input("Enter the list:"))
largest=lst[0]
smallest=lst[0]
for i in lst[1:]:
    if i > largest:
        largest=i
    if i < smallest:
        smallest=i
print(f"largest={largest}and smallest={smallest}")
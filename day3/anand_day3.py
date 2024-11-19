'''author:Anand Krishna M A
description:Display the multiplication table for a user-input number'''

num=int(input("Enter the number:"))
for i in range(1,11):
    print(num*i,end=' ')
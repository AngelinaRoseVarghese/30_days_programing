#Author=John
#Description: To Display the multiplication table for a user-input number.

num=int(input("Enter the number:"))
for i in range(1,11):
    multiplication=num*i
    print(multiplication,end=" ")
'''
Author: Anand Krishna M A
Description:  a program that takes two numbers (start and end) from the user and calculates the sum of all integers between those numbers using a for loop'''
start=int(input("Enter a starting no:"))
end=int(input("Enter a ending no:"))
result=0
for i in range(start,end+1):
    result+=i
print(result)
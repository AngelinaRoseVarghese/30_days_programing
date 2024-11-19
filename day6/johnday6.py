'''

Author: John Kuriakose
Description:A program that takes two numbers (start and end) from the user and
calculates the sum of all integers between those numbers using a for loop.
'''

start=int(input("Enter a starting number: "))
end=int(input("Enter a ending number: "))
result=0
for i in range(start,end+1):
    result=result+i
    print(result,",", end=" ")


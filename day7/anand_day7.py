'''author:Anand Krishna M A
Description:A program to Count the number of vowels in a string using for loop and if statement'''

word=input("Enter a sentence or word:")
count=0
for i in word:
    if i in 'aeiouAEIOU':
        count+=1
print("number of vowels = ",count)
'''
Date:25/11/2024
Author:Angelina Rose Varghese
Description:Write a program that takes two lists as input from the user.
Create a third list where:
All the even numbers from both lists appear first, sorted in ascending order.
Followed by all the odd numbers from both lists, also sorted in ascending order
'''
import math
prime=[]
not_prime=[]
no_num=int(input("How many numbers you want to enter: "))
for i in range(no_num):
    num=int(input("Enter a number: "))
    if num>1:
        is_prime = True
        for j in range(2,int(math.sqrt(num)+1)):
            if(num%j==0):
                is_prime=False
                break
        if is_prime:
            prime.append(num)
        else:
            not_prime.append(num)
prime.sort()
not_prime.sort()
new=prime+not_prime
print ("prime numbers are ",prime)
print ("numbers not prime are ",not_prime)
print(new)




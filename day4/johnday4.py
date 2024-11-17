#Author=John Kuriakose
'''Description:A program that uses a while loop to count
down from a number entered by the user to zero'''
num=int(input("Enter the number:"))
while num>0:
    num=num-1
    print(num,end=" ")
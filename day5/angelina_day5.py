'''
Date:13/11/2024
Author: Angelina Rose Varghese
Description:  a program that asks the user to input marks (0-100).
then prints the grade based on the following:
90-100: A
70-89: B
50-69: C
40-49: D
Below 40: F
'''
mark=int(input("Enter mark: "))
if (mark>=90 and mark<=100):
    print("A Grade")
elif (mark>=70 and mark<=89):
    print("B Grade")
elif (mark>=50 and mark<=69):
    print("C Grade")
elif (mark>=40 and mark<=49):
    print("D Grade")
elif mark<40:
    print("F Grade")
else:
    print("Invalid mark")
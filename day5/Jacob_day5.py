'''
Author: Jacob Thomas
Date:17/11/2024
Description: Write a program that asks the user to input marks (0-100) and then prints the grade
'''
mark= int(input("Enter the score"))
if (mark>= 90 and mark<=100) :
    print("A Grade")
elif(mark>=80 and mark<=89):
    print(" B Grade")
elif(mark>=70 and mark<=79):
    print("C Grade")
elif(mark>=60 and mark<-69):
    print("D Grade")
elif(mark>=50 and mark<=59):
    print("E Grade")
else:
    print("Fail")
'''Author:John Kuriakose
Date:17/11/2024
Description: Write a program that asks the user to input marks (0-100)
 and then prints the grade based on the following:'''

mark=int(input("Enter the mark:"))
if (mark>=90 and mark<=100):
    print("GRADE A")
elif (mark>=70 and mark<=89):
    print("GRADE B")
elif (mark>=50 and mark<=69):
    print("GRADE C")
elif (mark>=40 and mark<=59):
    print("GRADE D")
elif(mark<40):
    print ("GRADE F")
else:
    print("INVALID MARK")
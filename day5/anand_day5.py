'''Description:program that asks the user to input marks (0-100) and then prints the grade
author: Anand krishna M A'''


mark=int(input("Enter your marks:"))
if mark >=90:
    print("A Grade")
elif mark>=70:
    print("B Grade")
elif mark>=50:
    print("C Grade")
elif mark>=40:
    print("D grade")
else:
    print("E Grade")
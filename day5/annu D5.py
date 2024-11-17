m=int(input("Enter your mark"))
if (m>=90 and m<=100):
    print("Your grade is A")
elif(m>=70 and m<=89):
    print("Your grade is B")
elif(m>=50 and m>=69):
    print("Your grade is C")
elif(m>=40 and m>=49):
    print("Your grade is D")
elif(m<=40):
    print("Your grade is F")
else:
    print("invalid m")
import math
lst=eval(input("Enter the list:"))
sq_lst=[]
for i in lst:
    sq=math.pow(i,2)
    sq_lst.append(sq)
print(f"Square of list of numbers from given list={sq_lst}")
#Author=John Kuriakose
#Description:Input a list of numbers and get the square of the list as output

import math
my_list=[]
num=int(input("Number of values  you want to enter: "))
for i in range(num):
    sqrt_num=int(input("Enter the values: "))
    my_list.append(math.sqrt(sqrt_num))
print (my_list)
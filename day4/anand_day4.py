'''author:Anand Krishna M A
Description:program to count down from a given number'''

import time
time1=int(input("Enter the time from the countdown should starts:"))
for i in range(time1,0,-1):
    print(i)
    time.sleep(1)
print("Time UP!")
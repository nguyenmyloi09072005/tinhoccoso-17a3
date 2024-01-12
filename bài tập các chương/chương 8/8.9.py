# xây dựng chương trình count down
import time
n=int(input('nhập n:'))
while(n>0):
    time.sleep(1)
    n-=1
    print(n)
    if (n==0):
        print("start!!!")




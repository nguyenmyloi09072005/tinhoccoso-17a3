n=int(input('nhập vào n:'))   
s=1
for i in range(1,n+1):
    if (i%3==0):
        s*=i
print(s) 
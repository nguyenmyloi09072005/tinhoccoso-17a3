n=int(input('nhập vào n:'))   
s=0
for i in range(1,n+1):
    if i%2==0:
        s+=i
print(s)  
# không sử dụng hàm
n=int(input('nhập vào n:'))
uoc=[]
tong_uoc=0
so_luong_uoc=0
for i in range(1,n+1):
    if n%i==0:
        uoc.append(i)
        tong_uoc+=i
        so_luong_uoc+=1
print(uoc)
print(tong_uoc)
print(so_luong_uoc)
    
       
    

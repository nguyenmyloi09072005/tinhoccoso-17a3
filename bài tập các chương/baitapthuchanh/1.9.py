#HÀM KIỂM TRA UCLN CỦA 2 SỐ A VÀ B
def ucln(a,b):
    while(a!=b):
        if (a>b):
            a-=b
        else:
            b-=a
    return a
x=int(input('nhập n:'))  
y=int(input('nhập n:'))  
if ucln(x,y):
  print(x,'đây là ucln')
  
    


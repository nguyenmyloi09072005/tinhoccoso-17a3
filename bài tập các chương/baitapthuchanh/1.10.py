#HÀM TÍNH BCNN CỦA A VÀ B
def bcnn(a,b):
    m = a*b
    while a!= b:
        if a>b:
            a-= b
        else:
            b-= a
    m/= a    
    return m
x = int(input('nhập n:'))  
y = int(input('nhập n:')) 
result=bcnn(x,y) 
if bcnn(x,y):
  print(f'{result} là bcnn')
      
# # xây dựng chương trình nhập từ bàn phím 2 số nguyên a,b.Tìm BCNN(a,b)
a=int(input('nhập vào a:'))
b=int(input('nhập vào b:'))
# gợi ý tìm ucln rồi =>bcnn=a*b/ucln
while True:
    if(a>b):
        a-=b
    elif(b>a):
        b-=a
    else:
        break
         
print('bcnn là ',(a*b)/ucln)
# xây dựng chương trình nhập từ bàn phím 2 số nguyên a,b.Tìm UCLN(a,b)
a=int(input('nhập vào a:'))
b=int(input('nhập vào b:'))
# dùng phép toán trừ
while True:
    if(a>b):
        a-=b
    elif(b>a):
        b-=a
    else:
        break
print(f'ucln là:{a}')
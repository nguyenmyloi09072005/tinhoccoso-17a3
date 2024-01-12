
#E = tổng các số nguyên tố nhỏ hơn hay bằng n
n = int(input("Nhap vao so nguyen duong n: "))
tong = 0
i=0
j=0
for i in range(2, n+1):
    for j in range(2,i):
        if i%j == 0:
            break
        else:
            tong = tong + i
    print(tong)
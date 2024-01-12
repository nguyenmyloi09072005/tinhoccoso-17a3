#B = tổng các số chẵn nhỏ hơn hay bằng n
n = int(input("Nhap vao so nguyen duong n: "))
tong = 0
for i in range(0, n+1):
    if i%2==0:
        tong = tong + i
print(f"B = {tong}")
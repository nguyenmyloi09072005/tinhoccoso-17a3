# tổng chuỗi đan dấu
n = int(input("Nhap vao so nguyen duong n: "))
tong = 0.0
flag = True
for i in range(1, n+1):
    if flag == True:
        tong = tong + 1.0/i
        flag = False
    else:
        tong = tong - 1.0/i
        flag = True
print(f"F = {tong}")
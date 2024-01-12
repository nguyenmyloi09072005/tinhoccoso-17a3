# 1+2+3+...+n>A
# nhập A ,tìm n 
a = int(input("nhap a: "))
s = 0
n = 0
while True:
    if s > a:
        break
    n += 1
    s += n
print(n)
#t n nhỏ nhất sao cho 1+2^2+..+n^2>A
a = int(input("nhap a: "))
s = 0
n = 0
while True:
    if s > a:
        break
    n += 1
    s += n**2
print("n nho nhat: ", n)

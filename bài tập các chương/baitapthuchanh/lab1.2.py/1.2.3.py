# tìm số nguyên lớn nhất sao cho 1+2+...+m<A
a = int(input("nhap a: "))
s = 0
m = 0
while True:
    m += 1
    s += m
    if s >= a:
        m -= 1
        break
print("m lon nhat:", m)

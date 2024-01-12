# tìm số nguyên dương nhỏ nhất sao cho B=1+2^2+3^2+...+n^2>a
a=int(input('nhập vào giá trị a:'))
tong=0
n=0
while True:
    if tong>a:
        break
    n+=1
    tong+=n**2
print(f'số nguyên dương nhỏ nhất{n}')
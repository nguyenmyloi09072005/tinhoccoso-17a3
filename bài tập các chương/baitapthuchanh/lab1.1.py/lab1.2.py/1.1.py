# nhập vào số nguyên dương A
# tìm số nguyên dương n nhỏ nhất sao cho 1+2+3+....+n>A
a=int(input('nhập vào giá trị a:'))
tong=0
n=0
while True:
    if tong>a:
        break
    n+=1
    tong+=n
print(f'giá trị nn của n là{n}')
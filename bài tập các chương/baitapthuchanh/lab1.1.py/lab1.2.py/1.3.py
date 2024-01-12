# tìm số nguyên dương m lớn nhất 1+2+3+..+m<a
a=int(input('nhập vào giá trị a:'))
m=0
s=0
while True:
    m+=1
    s+=m
    if s>=a:
        m-=1
    print(m)


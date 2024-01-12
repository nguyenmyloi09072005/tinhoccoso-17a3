a=int(input('nhập vào giá trị a:'))
tich=1
n=0
while True:
    if tich>a:
        break
    n+=1
    tich*=n
print(f'giá trị nn của n là {n}')
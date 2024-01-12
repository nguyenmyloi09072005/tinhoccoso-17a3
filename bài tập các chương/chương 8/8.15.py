# tính tổng của các số nguyên nhập vào ,chấm dứt khi nhập vào số 0
tổng=0
while True:
    n=int(input('nhập một số nguyên(kết thúc là số 0):'))
    tổng+=n
    if (n==0):
        break
print(f'tổng là:{tổng}')
    

    

    
    
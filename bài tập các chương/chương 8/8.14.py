# Tính tổng n số nguyên nhập  vào
'''yêu cầu: xây dựng chương trình tính tổng của N số nguyên nhập vào '''
n=int(input('nhập vào số nguyên n:'))
S=0
for i in range(1,n+1):
    k=int(input(f'nhập số nguyên thứ {i}:'))
    S+=k
print(f'tổng {S}')

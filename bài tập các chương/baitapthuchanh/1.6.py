#HÀM KIỂM TRA SỐ FIBONACCI
# 0 1 1 2 3 5 8 13 21 34 ...
def so_fibonacci(n):
    a=0
    b=1
    while a<=n:
        if a==n:
            return True
        t=a
        a=b
        b=t+a
    return False
n=int(input('nhập giá trị n'))
if(so_fibonacci(n)):
    print(n,'là số fibonacci')
else:
    print(n,'ko phải')
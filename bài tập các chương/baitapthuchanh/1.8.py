#HÀM KIỂM TRA SỐ HARSHAD
# ví du 12=1+2  => 12%3==0 :là số harshad
def so_harshad(n):
    t=0
    a=n

    if n<0:
        return False
    while n!=0:
        t+=n%10
        n=n//10
    if a%t==0:
        return True
# n=int(input('nhập vào giá trị n:'))
# if (so_harshad(n)):
#     print(n,'là số harshad')
# else:
#     print(n,'không là số harshad')
def lietke(giới_hạn):
    ds_hsh=[i for i in range(giới_hạn) if so_harshad(i)]
    return ds_hsh
các_số_hsh=lietke(1000)
print(các_số_hsh)






    




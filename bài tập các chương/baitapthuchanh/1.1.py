#KIỂM TRA SỐ NGUYÊN TỐ
def so_ngto(n):
    flag=True
    if n<1:
        flag=False
    for i in range (2,n+1):
        if n%i==0:
            flag=False
            break
        return flag
so=int(input('nhập n:'))   
if so_ngto(so):
   print(so,'đây là số ngto')
else:
    print(so,'đây kp là số ngto')   
# liệt kê số nguyên tố <1000
def liet_ke_so_ngto(giới_hạn):
    day_so_ngto=[i for i in range(giới_hạn) if so_ngto(i)]
    return day_so_ngto
cac_so_ngto = liet_ke_so_ngto(1000)
print('dãy số ngto <1000',cac_so_ngto)


    
    
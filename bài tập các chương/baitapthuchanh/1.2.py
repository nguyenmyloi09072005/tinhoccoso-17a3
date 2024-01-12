#HÀM KIỂM TRA SỐ CHÍNH PHƯƠNG
def so_chinh_phuong(number):
    if number<0:
        return False
    flag=False
    for i in range (1,number+1):
        if i*i==number:
            flag=True
            break
    return flag
n=int(input('nhập n:'))
if(so_chinh_phuong(n)):
    print('là scp')
else:
     print('kp scp')

#liệt kê số chính phương <1000
# def liet_ke_scp(giới_hạn):
#     ds_scp=[i for i in range(giới_hạn) if so_chinh_phuong(i)]
#     return ds_scp
# số_chính_phương_dưới_1000=liet_ke_scp(1000)
# print('scp dưới 1000 là:',số_chính_phương_dưới_1000)
# hàm ktra scp
       

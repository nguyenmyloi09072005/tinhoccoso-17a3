#KIỂM TRA SỐ CHẮN
def so_chẵn(number):
    if number%2==0:
        return True
    else:
        return False
# n=int(input('nhập n:'))
# if so_lẻ(n):
#    print(n,'đây là số chẵn')
# else:
#     print(n,'đây kp là số chẵn') 
# def liet_ke_so_chẵn(giới_hạn):
#     ds_sc=[i for i in range(giới_hạn) if so_chẵn(i)]
#     return ds_sc
# số_chẵn_dưới_1000=liet_ke_so_chẵn(1000)
# print('sc dưới 1000 là:',số_chẵn_dưới_1000)
def liet_ke_so_chẵn(giới_hạn1,giới_hạn2):
    ds_sc=[i for i in range(giới_hạn1,giới_hạn2) if so_chẵn(i)]
    return ds_sc
số_chẵn=liet_ke_so_chẵn(5,10)
print('sc dưới 1000 là:',số_chẵn)

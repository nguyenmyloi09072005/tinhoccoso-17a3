#KIỂM TRA SỐ LẺ
def so_lẻ(number):
    if number%2!=0:
        return True
    else:
        return False
# n=int(input('nhập n:'))
# if so_lẻ(n):
#    print(n,'đây là số lẻ')
# else:
#     print(n,'đây kp là số lẻ') 
def liet_ke_so_le(giới_hạn):
    ds_sl=[i for i in range(giới_hạn) if so_lẻ(i)]
    return ds_sl
số_lẻ_dưới_1000=liet_ke_so_le(1000)
print('sl dưới 1000 là:',số_lẻ_dưới_1000)

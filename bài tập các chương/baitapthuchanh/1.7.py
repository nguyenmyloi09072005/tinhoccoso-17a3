#HÀM KIỂM TRA SỐ ĐỐI XỨNG
# kiểm tra số đối xứng
def doi_xung(n):
    flag= True            
    if str(n) !=str(n)[::-1]:
      flag=False         
    return flag

# so=int(input('nhập n:'))  
# if doi_xung(so):
#    print(so,'đây là đối số')
# else:
#     print(so,'đây là không phải')
    
def liet_ke_dx(giới_hạn):
    ds_dx=[i for i in range(giới_hạn) if doi_xung(i)]
    return ds_dx
dx_dưới_1000=liet_ke_dx(1000)
print('dx dưới 1000 là:',dx_dưới_1000)
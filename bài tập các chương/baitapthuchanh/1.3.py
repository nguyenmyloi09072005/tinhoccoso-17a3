#KIỂM TRA SỐ HOÀN HẢO
def so_hoan_hao(number):
    if number>1:
        tổng=0
        for i in range(1,number):
            if number%i==0:
                tổng+=i
        return tổng==number
# n=int(input('nhập n:'))
# if(so_hoan_hao(n)):
#     print('là số hoàn hảo')
# else:
#     print('kp số hoàn hảo')
def liet_ke_so_hoan_hao(giới_hạn):
    ds_shh=[i for i in range(giới_hạn) if so_hoan_hao(i)]
    return ds_shh
số_hoan_hao_dưới_1000=liet_ke_so_hoan_hao(1000)
print('shh dưới 1000 là:',số_hoan_hao_dưới_1000)

    
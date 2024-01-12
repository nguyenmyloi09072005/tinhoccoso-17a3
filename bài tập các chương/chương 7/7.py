a=int(input("số tiền muốn đổi là :"))
số_tờ_1=a//500000
tiền_còn_lại=a%500000
số_tờ_2=tiền_còn_lại//200000
tiền_còn_lại_2=tiền_còn_lại%200000
số_tờ_3=tiền_còn_lại_2//100000
tiền_còn_lại_3=tiền_còn_lại_2%100000
số_tờ_4=tiền_còn_lại_3//50000
tiền_thừa=tiền_còn_lại_3%50000
print("số tờ 500000 là:", số_tờ_1)
print("số tờ 200000 là:", số_tờ_2)
print("số tờ 50000 là:", số_tờ_3)
print("số tờ 50000 là:", số_tờ_4)
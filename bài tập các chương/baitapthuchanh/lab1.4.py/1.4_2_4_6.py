n=input('nhập chuỗi:')
#1.4.2 đảo chuỗi
daonguocptu=n[::-1]
print(daonguocptu)
#1.4.4
old_char=input('nhập từ cần thay:')
new_char=input('nhập từ thay vào:')
chuoi_moi=n.replace(old_char,new_char)
print(chuoi_moi)
#1.4.6
# nhập vào chuỗi được phân cách thành dấu phẩy
# tách chuỗi trên thành một ds các từ r in ra
n=input('nhập chuỗi:')
tachchuoi=n.split()
print(tachchuoi)
for i in tachchuoi:
    print(i.strip())
    
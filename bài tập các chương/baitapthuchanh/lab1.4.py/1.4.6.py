# nhập vào chuỗi được phân cách thành dấu phẩy
# tách chuỗi trên thành một ds các từ r in ra
n=input('nhập vào 1 chuỗi:')
tachchuoi=n.split()
print(tachchuoi)
for i in tachchuoi:
    print(i.strip())
    
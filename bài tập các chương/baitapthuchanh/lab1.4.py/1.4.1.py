'''viết một chương trình nhập vào chuỗi 'Python is fun' 
1.cho biết độ dài của chuỗi
2.in đảo ngược chuỗi này
3.chuyển chuỗi đã nhập sang chữ hoa (ko dùng upper)
4.hãy nhập vào 1 từ để thay thế từ fun
'''
n=input('nhập chuỗi:')
dodai=len(n)
print(f'độ dài của chuỗi là {dodai}')
#2.cách 1
daonguoc=''.join(reversed(n))
print(f'đảo ngược từ là {daonguoc}')
#cách 2
daonguocptu=n[::-1]
print(daonguocptu)
#3.
# dùng ord để lấy mã ASCII rồi chuyển về chữ hoa
# Chuyển chuỗi sang chữ hoa
uppercase_string = ""

for i in n:
    if 'a' <= i <= 'z':
        # Nếu là chữ cái thường, chuyển thành chữ cái hoa bằng cách thay đổi mã ASCII
        uppercase_char = chr(ord(i) - ord('a') + ord('A'))
    else:
        # Nếu không phải chữ cái thường, giữ nguyên ký tự
        uppercase_char = i

    uppercase_string += uppercase_char

print(f"Chuỗi chữ hoa là: {uppercase_string}")
#4.
old_char=input('nhập từ cần thay:')
new_char=input('nhập từ thay vào:')
chuoi_moi=n.replace(old_char,new_char)
print(chuoi_moi)


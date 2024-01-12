'''Cho chuỗi " Hello, Python! "
hãy viết ctrinh loại bỏ khoảng trắng ở trong chuỗi để trả về chuỗi hơpj lệ
(không có khoảng trắng ở đầu, cuỗi và mỗi từ chỉ cách nhau đúng 1 kí tự trống)'''
n=input('nhập vào chuỗi đã cho:')
no_whilespace=n.replace(" ","")
print('chuỗi đã sưar:',no_whilespace)
# cách 2 là tách ra rồi ghép lại
words=n.split()
No="".join(words)
print(No)
'''sử dụng try...except
cú pháp:
        try:   # khối lệnh có khả năng chạy ra lỗi
              
        except [loại lỗi as tên_biến_báo_lỗi]:
                  # in thông báo lỗi      '''
# ví dụ 14.2.2.1
x,y=5,0
try:
    print('x/y=',x/y)
except ZeroDivisionError as er:
    print('Error:',er)
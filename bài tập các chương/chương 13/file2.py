
# f = open('file1.txt', 'a+')
# f.write("Hello, we are Python")
# f.close()
#f = open ('vidu1.txt','r',encoding='utf-8')
#a = f.readline()   #readline:đọc 1 dòng từ 1 file ,tối đa là N byte,nếu k viết N 
                   #thì trả về str là dữ liệu được đọc tới khi nào gặp kí tự hết dòng hoặc hết file
#print('nội dung dòng đầu',a)
# readlines đọc các dòng cho đến hết file 
'''vídu về con trỏ tập tin ,hàm tell(),seek()'''
f = open ('vidu1.txt',"r+",encoding='utf-8')
a = f.read(5)  #dọc 12 kí tự đầu
print('nội dung là:\n',a)
b = f.tell()  # kiểm tra vị trí hiện tại
print('ví trí hiện tại là:',b)
f.seek(0)   # đặt lại vị trí con trỏ tại vị trí đầu file
c = f.read(12)
print('các kí tự đọc được sau khi về vị trí đầu tiên:\n',c)


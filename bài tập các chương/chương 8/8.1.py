# tìm số lớn nhất-nhỏ nhất
#bài1:a,b,c,d là 4 số được nhập vào từ bàn phím.Viết ctrinh tìm số lớn nhất và số nhỏ nhất
a=int(input('nhập vào giá trị a:'))
b=int(input('nhập vào giá trị b:'))
c=int(input('nhập vào giá trị c:'))
d=int(input('nhập vào giá trị d:'))
h=0 # biến để tăng lên
g=0 # giá trị lớn nhất
while(h<a) or (h<b) or (h<c) or (h<d):
    h+=1
    g=h
print('số lớn nhất',g)
# nhỏ nhất tương tự làm đi
# sau khi học xong toàn bộ chương trình ta có thể dùng hàm min max
a=int(input('nhập vào giá trị a:'))
b=int(input('nhập vào giá trị b:'))
c=int(input('nhập vào giá trị c:'))
d=int(input('nhập vào giá trị d:'))
max_number=max(a,b,c,d)
print('số lơn nhất là',max_number)
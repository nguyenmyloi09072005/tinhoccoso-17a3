# kiểm tra năm nhuận
a=int(input('nhập năm :'))
if (a%4==0) and (a%100!=0) :
    print('đây là năm nhuận')
elif(a%400==0):
    print('đây là năm nhuận')
else:
    print('đây không là năm nhuận')




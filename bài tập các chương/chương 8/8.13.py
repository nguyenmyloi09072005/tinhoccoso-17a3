'''nhập vào một số nguyên n tính các biểu thức sau
A= tổng các số lẻ nhỏ hơn hay bằng n
B= tổng các số chẵn nhỏ hơn hay bằng n
C=tích các số từ 1 đến n
D=tích các số chia hết cho 3 nhỏ hơn hay bằng n
E= tổng các số nguyên tố nhỏ hơn hay bằng n
F= tổng chuỗi đan dấu'''
#a
n=int(input('nhập n:'))
# A=0
# for i in range(1,n+1,2):
#     A+=i
# print('tổng các số lẻ là',A)
# B=0
# for i in range(2,n+1,2):
    #B+=i
# print('tổng các số lẻ là',B)
# C=1
# for i in range(1,n+1,1):
#     C*=i
# print('tích các số là:',C ) 
# D=1
# for i in range(1,n+1,1):
#     if (i%3==0):
#         D*=i
#         print(D)
E=0
for i in range(1,n+1,1):



    "#F = tổng chuỗi đan dấu\n",
    "n = int(input(\"Nhap vao so nguyen duong n: \"))\n",
    "tong = 0.0\n",
    "flag = True\n",
    "for i in range(1, n+1):\n",
    "    if flag == True:\n",
    "        tong = tong + 1.0/i\n",
    "        flag = False\n",
    "    else:\n",
    "        tong = tong - 1.0/i\n",
    "        flag = True\n",
    "print(f\"F = {tong}\")"
         





     
    

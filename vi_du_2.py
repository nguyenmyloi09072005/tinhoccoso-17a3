#Chương trình thứ 2.
print("đây là chương trình thứ 3")
print("Chương trình này được soạn thảo bằng IDE visual Studio Code.")
#bài 1.2
x=10
y=5
tổng=x+y
hiệu=x-y
tích=x*y
thương=x/y
print("tổng của",x, "+", y, "=", tổng)
print("hiệu của",x, "-", y, "=", hiệu)
print("tích của",x, "*", y, "=", tích)
print("thương của",x, "/", y, "=", thương)
#bài 1.3
ten_hang="sữa hộp vina milk"
so_luong=5
don_gia=25.000
tiền=so_luong*don_gia
print("tiền phải trả",don_gia, "*", so_luong, "=", tiền) 
#Bài 1.1
print("**    **  ******  **      **      ******")
print("**    **  **      **      **      **  **")
print("********  ******  **      **      **  **")
print("**    **  **      **      **      **  **")
print("**    **  ******  ******  ******  ******")
#bài 4
a,b,c=map(float,input("mời nhập độ dài 3 cạnh: ").split())
chuvi=a+b+c
p=chuvi/2
import math
dientich=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Dien tich la %.2f" %dientich)

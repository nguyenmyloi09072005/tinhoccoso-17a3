# xây dựng hàm
# ví dụ xấy dựng hàm tính điểm trung bình học kì 1 và học kì 2.in ra kq trực tiếp trong function
hk1=float(input('điểm tb hk1:'))
hk2=float(input('điểm tb hk2:'))
def hàm_tính_điểm_tb(a,b):
    dtb=float((hk1+hk2*2)/3)
    print('diem trung binh nam la:',dtb)
    return True
hàm_tính_điểm_tb(hk1,hk2)



# đọc file diem_tot_nghiep_2023.csv ra list
from csv import reader
with open('diem_tot_nghiep_2023.csv','r',encoding='utf-8') as read_obj:
    csv_reader=reader(read_obj)
    list_kq=list(csv_reader)
    print(list_kq)
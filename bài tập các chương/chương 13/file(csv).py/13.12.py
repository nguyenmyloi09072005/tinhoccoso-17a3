#đọc file data_1.csv theo dòng và in ra dòng
from csv import reader
with open('diem_tot_nghiep_2023.csv','r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        print(row)

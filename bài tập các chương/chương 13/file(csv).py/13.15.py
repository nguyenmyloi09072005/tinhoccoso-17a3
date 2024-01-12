# mở-ghi file csv
# cú pháp mở: f = open(filename, filemode, newline='')
# cú pháp ghi: csv.writer(f).writerow(content)
#13.15 mở-ghi danh sách-đóng file
import csv
def write_csv_file(filename,listContent):
    f= open(diem_tot_nghiep_2023.csv,'a',newline='123')
    for item in listContent:
        csv.write(f).writerow(item)
    f.close()
    print(listContent)
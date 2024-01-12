# mở đọc file csv
# cú pháp mở: f = open (file name)
# cú pháp đọc: csv.reader(f)
# cú pháp đóng : f.close()
# ví dụ 13.9
import csv
def read_csv_file(filename):
    f = open (filename)
    for row in csv.reader(f):
        print(row)
    f.close()    
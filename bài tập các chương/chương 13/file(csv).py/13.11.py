# mở đọc từng dòng nội dung theo từng cột-đóng file
def read_csv_file_côlumn(filename):
    f = open(filename)
    for row in csv.reader(f):
        print(row[0],'\t',row[1])
    f.close()
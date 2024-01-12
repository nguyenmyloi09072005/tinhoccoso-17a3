# mở-đọc từng dòng nội dung và đưa vào list
def read_csv_file_to_list(filename):
    f = open(filename)
    data= []
    for row in csv.reader(f):
        data.append(row)
        f.close()
        return data
    
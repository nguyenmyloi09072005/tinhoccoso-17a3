
# nếu bị lặp tên file sẽ bị lỗi=>dùng try finally
# try:
#     f = open('vidu1.txt','x')
# except Exception as e:
#    print(e)
# finally:
#    f.close()

with open("vidu1.txt",'w',encoding='utf-8') as f: 
        f.write('xin chào mỹ lợi \n')     # ghi nội dung vào tệp
        f.write('ngày hôm nay của bạn thế nào \n')
        f.write('việc học hành cuả bạn có ổn không \n')
        f.write('có thuận lợi như bạn mong muốn,dù sao thì hãy cố gắng hết mình nhé')
        f.close()






   
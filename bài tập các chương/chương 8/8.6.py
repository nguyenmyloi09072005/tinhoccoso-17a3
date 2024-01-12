# tính cước xe taxi
'''-dành cho xe 4 chỗ:
    giá mở cửa  11.000 đồng/0.8km
    trong phạm vi 20km  12.100 đ/km
    từ km thứ 21 trở đi  10.000 đ/km
    
    -dành cho xe 7 chỗ:
    giá mở cửa  13.000 đồng/0.8km
    trong phạm vi 30km  14.100 đ/km
    từ km thứ 31 trở đi  12.000 đ/km
    -tiền chờ :5 phút đầu được miễn phí,từ phút thứ sáu trở đi 800 đ/phút
    '''
a=float(input('nhập vào loại xe:'))
b=float(input('nhập vaò số km:'))
c=float(input('nhập vào thời gian chờ:'))
if (a==4):
    if(b<=20) and (c<=5):
        print('cước',b*12.100+11.000)
    elif(b>20) and (c<=5):    
        print('cước',(b-20)*10.000+20*12.100+11.000)
    elif(b<=20) and (c>5):
        print('cước',(b*12.100+11.000)+(c-5)*800)
    elif(b>20) and (c>5):    
        print('cước',(b-20)*10.000+20*12.100+11.000+(c-5)*800)
elif(a==7):
    if(b<=30) and (c<=5):
        print('cước',b*14.100+13.000)
    elif(b>30) and (c<=5):    
        print('cước',(b-30)*12.000+30*14.100+13.000)
    elif(b<=30) and (c>5):
        print('cước',(b*14.100+13.000)+(c-5)*800)
    elif(b>30) and (c>5):    
        print('cước',(b-30)*12.000+30*14.100+11.000+(c-5)*800) 
else:
     print('xe khác giá khác')   




    

    
         
   


    

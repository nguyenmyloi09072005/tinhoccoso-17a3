# viết chương trình nhập một số nguyên,dừng lại khi nhập 1 kí tự. đếm sl và tính tbc
s = 0
d=0
while True:
    n = input('n: ')
    if (len(n)<1 or not n.isdigit()):
        break
    else:
        s+=int(n)
        d+=1
print('tổng là:',s)
print('sluong',d)
if(d==0):
        print('không có tbc')
else:        print('tbc:',s/d)


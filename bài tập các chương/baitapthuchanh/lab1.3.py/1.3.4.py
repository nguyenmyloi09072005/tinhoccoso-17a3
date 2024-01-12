# xây dựng chương trình đảo ngược một dãy số với số lượng tùy ý  
# bắt đầu là số 1 và chỉ hiện ra các số lẻ or chẵn
# với nghĩa là số liên tục 
n=int(input('nhập vào số lượng phần tử trong dãy:'))
odd_sequence=(input('bạn muốn in ra lẻ (L) hay chẵn(C):'))
filter_sequence=[]
if odd_sequence=='L':
    filter_sequence=[i for i in range(1,n+1) if i%2!=0]
elif odd_sequence=='C':
    filter_sequence=[i for i in range(1,n+1) if i%2==0]
else:
    print('không có dãy số đó')
dao_nguoc=filter_sequence[::-1]
if filter_sequence:
    print(f'dãy số đảo ngược là {dao_nguoc}')
else:
    print('không có dãy số dảo ngược')

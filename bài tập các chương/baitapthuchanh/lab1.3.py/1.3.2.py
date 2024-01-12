# tìm các số thuộc [1000,2000] sao cho các số chia hết cho 3 và là số lẻ.
# in các số lên màn hình và các số cách nhau bởi dấu ,
for i in range(1000,2000+1):
    if i%3==0 and i%2!=0:
        print(i,end=',')
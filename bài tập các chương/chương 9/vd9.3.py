# biến cục bộ và biến toàn cục
#vidu về biến toàn cục
s='hello python'   # s ở đây là biến toàn cục
def in_s():
    print(s)
    return
print()
in_s()
# vidu về biến cục bộ
s='hello python'
def in_s():
    s='xin chào python'  # biến cục bộ
    print(s)
    return
in_s() # khi chạy nó sẽ in ra biến cục bộ
print(s)   # khi chạy sẽ in ra biến toàn cục


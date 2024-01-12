# xử lí ngoại lệ,...
'''cú pháp:
            try:      # khối mã có khả năng gây lỗi,khi lỗi xảy ra ,khối này sẽ bị dừng ở dòng gây lỗi
                except:    # đoạn mã xử lý lỗi,chỉ thực hiện nếu có lỗi xảy ra
                else:      # có thể xuất hiện ngay sau khối except cuối cùng đoạn mã sẽ được thực hiện
                             nếu không có except nào được thực hiện(đoạn try không có lỗi)  
            finally:       # còn được gọi là khối clean-up, luôn được thực hiện dù có xảy ra lỗi không      '''
# ví dụ quy tắc bắt ngoại lệ:lọt sàng xuống nia
try:
    #giả sử có một số code ở đây có thể ném ra nhiều loại ngoại lệ khác nhau
    value=int(input('nhập một số:'))
    result=10/value
except ValueError:  #bắt và xử lí ngoại lệ khi nhập giá trị không phải là sô
    print('đó không phải là một số hợp lê.')
except ZeroDivisionError:   # bắt và xử lí ngoại lệ khi chia cho 0
    print('lỗi chia cho 0')
except:    #bắt bất kì ngoại lệ nào khác không được xác định cụ thể ở trên
    print('không có lỗi xảy ra.kết quả là:',result)
finally: # chạy không phụ thuộc vào việc có lỗi xảy ra hay không
    print('hoàn thành xử lý ngoại lệ')





#viết funcion tính và trả về chỉ số BMI của một người dựa trên cân nặng
import math
def tinh_bmi(can_nang,chieu_cao):
    bmi=can_nang/math.pow(chieu_cao,2)
    print('chỉ số bmi của bạn là',bmi)
    return bmi
tinh_bmi(70,1.7)

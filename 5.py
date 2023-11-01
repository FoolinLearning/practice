# 英制单位英寸和公制单位厘米互换

# Version: 0.1
# Author: 骆昊

# value = float(input('请输入长度: '))
# unit = input('请输入单位: ')
# if unit == 'in' or unit == '英寸':
#     print('%f英寸 = %f厘米' % (value, value * 2.54))
# elif unit == 'cm' or unit == '厘米':
#     print('%f厘米 = %f英寸' % (value, value / 2.54))
# else:
#     print('请输入有效的单位')
value1=input('请输入长度:')
print(type(value1))
value = float(value1)
unit = input('请输入单位:')
print(unit)
print(type(unit))
if unit == 'cm' or unit == '厘米':
    print('%f厘米=%f英寸' % (value, value / 2.54 ))
elif unit == 'in' or unit == '英寸':
    print('%f英寸=%f厘米' % (value, value * 2.54))
else:
    print('请输入正确的单位')
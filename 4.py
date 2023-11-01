"""
分段函数求值
		3x - 5	(x > 1)
f(x) =	x + 2	(-1 <= x <= 1)
		5x + 3	(x < -1)

Version: 0.1
Author: 王敏瑞
"""

x = float(input("请输入x的值："))
if x > 1:
    y = 3 * x - 5
else:
    if x < -1:
        y = 5 * x + 3
    else:
            y = x + 2
print("f(%.2f)=%.2f" % (x,y))


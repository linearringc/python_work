import numpy as np
def gradient_descent(a, b, c):#三个初始变量 初始x、 步长x、循环次数
    x = a
    for i in range(c):
        gradient = x * 2
        x = x - gradient * b
        print(f"迭代{i+1}: x = {x:.4f}, 梯度 = {gradient:.4f}")
        if gradient < 1e-6:
            break
    return x

a1 = 10
b1 = 0.1
c1 = 100 #循环60次之后导数=0

result = gradient_descent(a1, b1, c1)
print(f"最终结果：{result:.6f}")

#x = a  放在循环前
#def a(): 定义函数
#for i in range(c): i变量名自定义
#引入新变量gradient = 2 * x 作为原函数的导数

#1e-6 = 0.0000001
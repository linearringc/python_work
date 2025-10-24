# Chapter 2 变量和简单数据类型
# 2.1
print("you are a cat. ") #打印 print("")

# 2.2 变量
message_2 = "you are a dog. "
print(message_2)

# 2.3.1 使用方法修改大小写
message_3 = "you are Abby"
print(message_3.title()) #首字母大写 .title()
print(message_3.upper()) #全部大写 .upper()
print(message_3.lower()) #全部小写 .lower()

# 2.3.2 在字符串中使用变量
message_4 = "Na"
message_5 = "yina"
message_6 = f"{message_4} {message_5}" #f字符串 f"{} {}"
message_7 = f"Hi, {message_4} {message_5}" #f字符串中的常量和变量
print(message_6)
print(f"Hi! {message_4} {message_5}") #print中的f字符串中的常量和变量
print(message_7)

# 2.3.3 空格和换行
print("\tNayina") #空格 \t
print("name:\nnayina\nzhangbing") #换行 \n

# 2.3.4 删除空白
message_8 = " Nayina "
print(message_8.strip()) # 删除左右两侧的空白 .strip()
print(message_8.lstrip()) # 删除左侧空白 .lstrip()
print(message_8.rstrip()) #删除右侧空白 .rstrip()
print(message_8)
message_8 = message_8.strip()
print(message_8)

# 2.4.1 整数
print(2 + (2+3)*4 - 6/3 + 6**2) #加 +减 -乘 *除 /平方 **

# 2.4.5 同时给多个变量赋值
x, y, z = 0, 0, 0

# 2.4.6 常量
NAYINA = "Mom"


# Chapter 3 列表简介
# 3.1 列表
bicycles = ['trek','dahang', 'redline']
print (bicycles[0].title())

#3.2 修改添加和删除
#修改指定位置
bicycles = ['trek','dahang', 'redline']
bicycles[0] = 'brompton'
print (bicycles)
#在末尾添加 .append()
bicycles.append('maimai')
print (bicycles)
#在列表中插入 .insert()
bicycles.insert(0,'giant')
print (bicycles)
#在列表中删除 删除列表中任意值 del /删除列表里最后一个值 .pop()
del bicycles[1]
print (bicycles)
poped_bicycles = bicycles.pop(0)
print(bicycles)
print(poped_bicycles)
#根据值删除元素，只删除列表里的第一个值 .remove()
bicycles.remove('redline')
print(bicycles)

#3.3 组织列表
#永久性排序 字母顺序正序 .sort()/字母顺序倒序 .sort(reverse = True)
cars = ['audi', 'VW', 'bmw', 'toyota']
cars.sort(reverse = True)
print(cars)
#临时性排序 .sorted()
print(sorted(cars, reverse=True))
print(cars)
#倒着打印列表 就地反转列表的排列顺序，需要先反转再打印 .reverse()
cars.reverse()
print(cars)
#确定列表的长度 len()
print(len(cars))


#Chapter 4 操作列表
#4.1 遍历整个列表
magicians = ['Chenyi', 'Nayina', 'Huge', 'Airenkejie']
for magician in magicians:
    print(magician)

for magician in magicians:
    print(magician.lower() + ' is good!')

#4.3 创建数值列表 range()
for value in range (1,5):
    print(value)

#4.3.2 使用range指定步长
even_numbers =list(range(2,11,2))
print (even_numbers)

squares = []
for number in range(1,11):
    square = number**2
    squares.append(square)

print(squares)

squares = []
for number in range(1,11):
    squares.append(number**2)

print(squares)

#4.3.3 对数字列表执行简单的统计计算 最小值 min()/最大值 max()/总和 sum()
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

#4.3.4 列表解析
squares = [value**2 for value in range(1,11)]
print(squares)

#4.4.1 切片 [0:1]/ [:1]/ [1:]/ [-1:]
players = ['nayina', 'Chenyi', 'luoyonghao']
print(players[0:1])
print(players[:1])
print(players[1:])
print(players[-1:])

#4.4.2 遍历切片 for [0:3]
for player in players[0:3]:
    print(player.title())

#4.4.3 复制列表 [:] 新列表不随旧列表的改变而改变
new_players = players[:]
players.append('bobby')
print(players) #旧列表
print(new_players) #新列表

new_players1 = players #直接赋值，新列表随旧列表的改变而改变
print(new_players1)

#4.5 元组 值不可变的列表 ()
dimensions = (1,2)
print(dimensions[0])

for dimension in dimensions:
    print(dimension)





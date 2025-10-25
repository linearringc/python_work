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

numbers = [1, 2, 3]
numbers = [number + 1 for number in numbers]
print(numbers)

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

#4.5.3 给元组重新赋值
dimensions = (5,8)
print(dimensions)


#Chapter 5 if语句 if == else
players = [0, 1, 2]
for player in players:
    if player == 1:
        print('nayina')
    else:
        print('chenyi')
#检查相等时不考虑大小写 .lower() ==
players =['chenyi', 'Huchenfeng', 'Liting']
for player in players:
    if player.lower() == 'huchenfeng':
        print('banned')
    else:
        print('unbanned')
#检查是否不相等 !=
    if player != 'chenyi':
        print('dislike second hand iphone')

#5.2.5 检查多个条件 == and/or >=
#5.2.6 检查特定值是否包含在列表中 (not)in
#缩进的作用：如果测试通过了，执行if语句后面的所有代码行，否则将忽略他们
players2 =['chenyi', 'Huchenfeng', 'Liting']
user = 'amy'
if user not in players2:
    print('amy is not here!')
else:
    print('amy is here')

#5.3.2 判断多个条件 if elif else 只能判断一个条件，判断多个条件请用多个单独的if
ages= (1,29,34,66,78,99)
for age in ages:
    if age < 30:
        print('I am young')
    elif age < 80:
        print('I am felling good')
    else:
        print('so tired')
#5.4.2 检查列表不是空的
meals = []
if meals:#当列表至少包含一个元素时，python会返回true
    for meal in meals:
        print('do you want eggs?')
else:
     print('please arrange your order.')


#Chapter 6 字典 { , }可以将任何python对象作为字典的值
#6.2.1 访问字典的值
alien = {'meme':'bibithedog'}
print(alien['meme'])

#6.2.2 添加键值对 [] = ''
alien = {1:'amy', 2:'bomb', 3:'amy'}
alien[3] = 'cici'
alien[8] = 'vivi'
print (alien)

#6.2.5 删除键值对 del
del alien[2]
print (alien)

#6.3.1 遍历字典 for key, value in .items()
for key, value in alien.items():
    print(key,value)

#6.3.2 遍历字典中所有键 .keys()
for key in alien.keys():
    print(key)
#6.3.3 按顺序遍历字典中的所有键 .sorted()
for key in sorted(alien.keys()):
    print(key)

#6.3.4 遍历字典中所有值  .values()
for value in alien.values():
    print(value)
#去重 .set()
for value in set(alien.values()):
    print(value)

#6.4 嵌套
#6.4.1  字典列表
aliens = []
for alien in range(30):
    alien = {'color' : 'blue', 'name' : 'Chenyi'}
    aliens.append(alien)

for alien in aliens[:3]:
    alien['color'] = 'milk'
print(aliens)

#6.4.2 在字典中存储列表
pizza = {
    1 : 'apple',
    2 : ['banana', 'pear']
}
print(pizza[1])
for fruit in pizza[2]:
    print(fruit)

#6.4.3  在字典中存储字典
personal_profile = {
    'bini' : {
        'age' : 18,
        'eye_color' : 'blue',
        'job' : 'game tester'
    },

    'vivi' :{
        'age' : 19,
        'eye_color' : ['grey','white'],
        'job' : 'game tester lead'
    }
}
for value in personal_profile.values():
    eye_color = value['eye_color']#value[key] 键访问
    if isinstance(eye_color, list):  # 检查是否是列表
        for color in eye_color:  # 循环打印每个颜色
            print(color)
    else:  # 如果是字符串，直接打印
        print(eye_color)

#Chapter7 用户输入和while循环

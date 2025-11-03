#BMI计算器
height = int(input('your height (cm) : '))
weight = int(input('your weight (kg) : '))

BMI= weight / (height/100) ** 2
print('your BMI is: ' + str(BMI))

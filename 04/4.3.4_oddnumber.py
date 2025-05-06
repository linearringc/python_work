#list = [value for value in range(1,21,2)]
#print(list) 

#list = [value for value in range(3,31,3)]
#print(list)

#list = [value**3 for value in range(1,11)]
#print(list)

list = []
for value in range(1,11):
	list.append(value**3)
print(list)

print(list[0:-3])

for value in list[0:3]:
	print(value)

list2 = list[:]
print(list2)
list2.append('888')
print(list2)
print(list)

print("TOP3=" + str(list[0:3]))
print("MIDDLE3=" + str(list[4:7]))
print("LAST3=" + str(list[-3:]))
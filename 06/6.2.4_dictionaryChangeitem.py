from collections import OrderedDict

chenyi =OrderedDict()

chenyi = {'height':'183', 'age':'22', 'school':'collage'}
print(chenyi['height'])

chenyi['height'] = '159'
print(chenyi['height'])

chenyi['sex'] = 'male'
print(chenyi['sex'])

if chenyi['school'] == 'collage':
	chenyi['height'] = '173'
else:
	chenyi['height'] = '183'

print(chenyi['height'])

del chenyi['age']
print(chenyi)
age = input('請輸入你的年紀：')
age = int(age)
if age < 18:
	print('你不能開車')
elif age >= 18 and age < 65:
	print('你可以開車')
else:
	print('你太老了，不能開車')
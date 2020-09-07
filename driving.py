country = input('請問你是哪個國家: ')
age = input('請問你幾歲: ')
age = int(age) # 型別轉換 將字串轉成整數
if country == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
elif country == '美國': # elif 要跟在一個if 下面
	if age >= 16:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
else:
	print('你只能輸入台灣/美國喔')

# practice if in a row

driving = input('你有沒有開過車？')
if driving != '有' and driving != '沒有':
	print('請輸入有或沒有')
	raise SystemExit

age = input('請問你的年齡是幾歲？')
age = int(age)

if driving == '有':
	if age >= 18:
		print('你很棒')
	else:
		print('你犯法了')

else:
	if age >= 18:
		print('你為什麼不去考假照？')
	else:
		print('再過幾年你就可以考駕照了')
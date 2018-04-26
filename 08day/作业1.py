a = "123456"
d = "123456"
i = 1
while True:
	acc = input("请输入账号")
	pwd = input("请输入密码")
	if a == acc and d == pwd:
		choose_c = int(input("请选择英雄 0=ADC 1=肉 2=法师"))
		if choose_c == 0:
			print("鲁班大师")
		elif choose_c == 1:
			print("程咬金")
		elif choose_c == 2:
			print("王昭君")
		break
	else:
		print("error%d次"%i)
		i+=1
		if i == 4:
			print("账号被封")
			break

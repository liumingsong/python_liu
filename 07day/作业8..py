s_acc = "123456"
s_pwd = "abc"
s_my = 1000
acc = input("请输入账号")
pwd = input("请输入密码")
if s_acc == acc and s_pwd == pwd:
	my = float(input("请输入金额"))
	if my<=s_my:
		print('取款金额:%f,余额:%f'%(my,s_my-my))
	else:
		print('去你妈卖批')
else:
	print('无效账户')


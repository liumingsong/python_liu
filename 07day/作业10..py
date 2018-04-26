s_acc = "123123"
s_pwd = "111"
print("TIMI")
choose_login = int(input("请选择登录方式 1=qq 2=微信 3=账号"))


if choose_login == 1:
	print("qq登录成功")
	choose_hero = int (input("请选择英雄 1=战士 2=法师3=刺客4=辅助"))

	if choose_hero == 1:
		print("项羽")
	elif choose_hero == 2:
		print("妲己")
	elif choose_hero == 3:
		print("李白")
	elif choose_hero == 4:
		print("周公")


elif choose_login == 2:
	print("微信登录成功")
elif choose_login == 3:
	account = input("请输入账号")
	pwd = input("请输入密码")
	if account == s_acc and pwd == s_pwd:
		print("账号登录成功")
	else:
		print("登录失败")

s_acc = "123456"
s_pwd = "abc"
acc = input("请输入账号")
pwd = input("请输入密码")
if s_acc == acc and s_pwd == pwd:
	print("登入成功")
elif s_acc != acc and s_pwd == pwd:
	print("输入账号不对")
elif s_acc == acc and s_pwd != pwd:
	print("输入密码不对")

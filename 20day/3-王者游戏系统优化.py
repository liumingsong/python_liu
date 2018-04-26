list = []
def aegis():
	acc,pwd = cus_input()
	temp = check_acc(acc)
	if temp == None:
		dict = {}
		dict["acc"] = acc
		dict["pwd"] = pwd
		list.append(list)
		print("注册成功")
	else:
		print("注册失败")
def login():
	acc,pwd = cus_input()
	temp = check_acc(acc)
	if temp != None:
		if temp.get("status") == 1:
			print("账号在登入着")
		else:
			if pwd == temp["pwd"]:
				print("登入成功")
				temp["status"] = 1
			else:
				print("密码不对")
	else:
		print("账号不存在，请先注册")
def loginout():
	acc = int(input("请输入账号"))
	temp = check_acc(acc)
	if temp != None:
		if temp.get("status") == 1:
			print("账号退出成功")
			temp["status"] = 0
		else:
			print("傻逼呀")
	else:
		print("没有账号")
def cus_input():
	acc = int(input("请输入账号"))
	pwd = int(input("请输入密码"))
	return acc,pwd
def check_acc(acc):
	flag = 0
	for i in list:
		if acc == i["acc"]:
			flag = 1
			return i
	if flag == 0:
		return None
while True:
	fun= int(input("请选择功能 1注册 2登录 3登出 4退出"))
	if fun == 1:
		register()
	elif fun == 2:
		login()
	elif fun  == 3:
		loginout()

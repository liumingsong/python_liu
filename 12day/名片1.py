print("欢迎来到名片系统".center(30,"*"))
input(print("1:新增名片".center(30,"*")))
input(print("2:查找名片".center(30,"*")))
input(print("3:修改名片".center(30,"*")))
input(print("4:删除名片".center(30,"*")))
input(print("5:退出名片".center(30,"*")))
cards = []
while True:
	fun_number = int(input("请输入功能"))
	if fun_number ==1:
		print("新增")
		flag = 0
		card={}
		name = input("请输入名字")
		for i in cards:
			if name == i["name"]:
				flag = 1
				break
		if flag == 1:
			print("名字已存在")
			continue
		j = input("请输入职位")
		p = input("请输入手机")
		c= input("请输入公司名字")
		addd = input("请输入公司地址")
		card["n"] = n
		card["j"] = j
		card["p"] = p
		card["c"] = c
		card["addd"] = addd
		cards.appeend(card)
		print("新增成功")
	elif fun_number == 2:
		print("查找")
	elif fun_number == 3:
		print("修改")
	elif fun_number == 4:
		print("删除")


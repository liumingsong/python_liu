print("欢迎来到名片系统:".center(30," "))
print("1:新增名片".center(30," "))
print("2:查找名片".center(30," "))
print("3:修改名片".center(30," "))
print("4:删除名片".center(30," "))
print("5:退出名片系统".center(30," "))
cards = []
while True:
	a = int(input("请输入功能"))
	if a == 1:
		print("新增名片")
		flag = 0
		cards={}
		name = input("请输入名字")
		for temp in cards:
			if name == temp["name"]:
				flag = 1
				break
		if flag == 1:
			print("名字已经存在")
			continue
		job = input("请输入职位")
		phone = int(input("请输入电话号码"))
		company = input("请输入公司名称")
		address = input("请输入公司地址")
		card["name"] = name
		card["job"] = job
		card["phone"] = phone
		card["company"] = company
		card["address"] = address
		cards.append(card)
		print("新增成功")
	elif a == 2:
		print("查找")
		name = int(input("请输入名字"))
		flag = 0
		for temp in cards:
			if name == temp["name"]:
				flag = 1
				print("名字是:%s\n"%temp["name"],"职位是:%s\n"%temp["job"],"电话是:%s\n"%temp["phone"],"公司名称是:%s\n"%temp["company"],"公司地址是:%s\n"%temp["address"])

print("欢迎来到名片系统:".center(30,"*"))
print("1:新增名片".center(30," "))
print("2:查找名片".center(30," "))
print("3:修改名片".center(30," "))
print("4:删除名片".center(30," "))
print("5:退出名片".center(30," "))
cards = []
while True:
	a = int(input("请输入功能"))
	if a == 1:
		print("新增")
		flag = 0
		card={}
		name = input("请输入名字")
		for temp in cards:
			if name == temp["name"]:
				flag = 1
				break
		if flag == 1:
			print("名字已存在")
			continue
		job = input("请输入职位")
		phone = int(input("请输入电话"))
		company = input("请输入公司名字")
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
		name = input("请输入名字")
		flag = 0
#		count = 0
		for temp in cards:
			if name == temp["name"]:
#				count += 1
				flag = 1
				print("名字是:%s\n"%temp["name"],"职位是:%s\n"%temp["job"],"电话是:%s\n"%temp["phone"],"公司名字是:%s\n"%temp["company"],"公司地址是:%s\n"%temp["address"])

				break
		if flag == 0:
			print("查无此人")
#		else:
#			print("名字是:%s\n"%(cards[count-1]["name"]),cards[count-1]["job"],cards[count-1]["phone"],cards[count-1]["company"],cards[count-1]["address"])
	elif a == 3:
		print("修改".center(10,"*"))
		f = 0
		name = input("请输入你要修改的名字:")
		for i in cards:
			if name == i["name"]:
				f = 1
				lei = int(input("请输入修改类型:姓名(1),职位(2),电话(3),公司名称(4),公司地址(5):"))
				if lei == 1:
					while True:
						pan = 0
						names = input("请输入新名字:")
						for g in cards:
							if names == g["name"]:
								pan = 1
								print("名字重复，重新输入")
								break
						if pan == 0:
							i["name"] = names
							break
				elif lei == 2:
					i["job"] = input("请输入新职位:")
				elif lei == 3:
					i["phone"] = int(input("请输入新电话:"))
				elif lei == 4:
					i["company"] = input("请输入新公司名称:")
				elif lei == 5:
					i["address"] = input("请输入新公司地址:")
				else:
					print("输入有误")
				print("修改成功")
				break
			if f == 0:
				print("没有此人")
	elif a == 4:
		name = input("请输入你要删除的名字")
		flag = 0
		for temp in cards:
			if name == temp["name"]:
				flag = 1
				sure_nu = int(input("0确认删除,1返回系统"))
				if sure_nu == 0:
					cards.remove(temp)
					print("删除成功")
				break
		if flag == 0:
			print("无此人")
	elif a == 5:
		sure_num = int(input("0返回,1确认退出"))
		if sure_num == 0:
			print("退出成功")
			continue
		break

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
				print("姓名:%s\n职位:%s\n电话:%s\n公司名称:%s\n公司地址:%s\n"%(temp["name"],temp["job"],temp["phone"],temp["company"],temp["address"]))
#				print("名字是:%s\n"%temp["name"],"职位是:%s\n"%temp["job"],"电话是:%s\n"%temp["phone"],"公司名字是:%s\n"%temp["company"],"公司地址是:%s\n"%temp["address"])

				break
		if flag == 0:
			print("查无此人")
#		else:
#			print("名字是:%s\n"%(cards[count-1]["name"]),cards[count-1]["job"],cards[count-1]["phone"],cards[count-1]["company"],cards[count-1]["address"])
	elif a == 3:
		name = input("请输入你要修改的名字")
		for temp in cards:
			if name == temp["name"]:
				print("1:修改名字".center(30," "))
				print("2:修改职位".center(30," "))
				print("3:修改手机号".center(30," "))
				print("4:修改公司名称".center(30," "))
				print("5:需要改公司地址".center(30," "))
				ch_num = int(input("请选择修改内容:"))
				if ch_num == 1:
					name = input("请输入新的名字")
					temp["name"] = name
				elif ch_num == 2:
					job = input("请输入新的职位")
					temp["job"] = job
				elif ch_num == 3:
					phone = input("请输入新的手机好")
					temp["phone"] = phone
				elif ch_num == 4:
					company = input("请输入新的公司名称")
					temp["company"] = company
				elif ch_num == 5:
					address = input("请输入新的公司地址")
					temp["address"] = phone
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
					cardbs.remove(temp)
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

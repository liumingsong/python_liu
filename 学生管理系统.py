print("欢迎来到学生成绩管理系统".center(30,"*"))
print("1:录入成绩".center(30," "))
print("2:查询成绩".center(30," "))
print("3:修改成绩".center(30," "))
print("4:删除成绩".center(30," "))
print("5:打印全部成绩".center(32," "))
print("6:退出系统".center(30," "))
cards = []
while True:
	a = int(input("请选择功能"))
	if a == 1:
		flag = 0
		card={}
		num = int(input("请输入学号"))
		for temp in cards:
			if num == temp["num"]:
				flag = 1
				break
		if flag == 1:	
			print("学号已存在")
			continue
		name = input("请输入姓名")
		yuwei = float(input("请输入语文成绩"))
		shuxue = float(input("请输入数学成绩"))
		yingyu = float(input("请输入英语成绩"))
		card["num"] = num
		card["name"] = name
		card["yuwei"] = yuwei
		card["shuxue"] = shuxue
		card["yingyu"] = yingyu
		cards.append(card)
		print("录入成功")
		for i in cards:
			print(i)
	elif a == 2:
		print("查询成绩")
		num = int(input("请输入学号"))
		flag = 0
		for temp in cards:
			if num == temp["num"]:
				flag = 1
				print("学号是:%d\n姓名是:%s\n语文成绩是:%0.2f\n数学成绩是:%0.2f\n英语成绩是:%0.2f\n"%(card["num"],card["name"],card["yuwei"],card["shuxue"],card["yingyu"]))
				break
		if flag == 0:
			print("查无此人")
			continue
	elif a == 3:
		print("请输入你要修改的成绩")
		num = int(input("请输入你要修改的学号"))
		for i in cards:
			if num == i["num"]:
				print("1:修改学号".center(30," "))
				print("2:修改名字".center(30," "))
				print("3:修改语文成绩".center(32," "))
				print("4:修改数学成绩".center(32," "))
				print("5:修改英语成绩".center(32," "))
				f = int(input("请输入你要修改的选项:"))
				if f == 1:
					num = int(input("请输入新学号"))
					i["num"] = num
				elif f == 2:
					name = input("请输入新名字:")
					i["name"] = name
				elif f == 3:
					yuwei = float(input("请输入新语文成绩:"))
					i["yuwei"] = yuwei
				elif f == 4:
					shuxue = float(input("请输入新数学成绩:"))
					i["shuxue"] = shuxue
				elif f == 5:
					yingyu = float(input("请输入新的英语成绩"))
					i["yingyu"] = yingyu
			else:
				print("查无此人")
	elif a == 4:
		num = int(input("请输入删除的学号"))
		flag = 0
		for temp in cards:
			if num == temp["num"]:
				flag = 1
				sure_num = int(input("0确认删除,1返回功能"))
				if sure_num == 0:
					cards.remove(temp)
					print("删除成功")
				break
		if flag == 0:
			print("查无此人")
	elif a == 5:
		print("打印")
		print("学号\t名字\t语文\t数学\t英语\t")
		for i in cards:
			print("%d\t%s\t%0.2f\t%0.2f\t%0.2f\t"%(i["num"],i["name"],i["yuwei"],i["shuxue"],i["yingyu"]))
	elif a == 6:
		sure_num = int(input("1确认退出,0返回功能"))
		if sure_num == 0:
			print("退出成功")
			continue
		break


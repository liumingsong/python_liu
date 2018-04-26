print("欢迎进入水果进出系统".center(30,"*"))
print("1:进入水果名单".center(30," "))
print("2:查看水果数量".center(30," "))
print("3:调整水果数量".center(30," "))
print("4:去除此类水果".center(30," "))
print("5:打印水果类型".center(30," "))
print("6:退出水果系统".center(30," "))
cards = []
while True:
	a = int(input("请选择功能"))
	if a == 1:
		flag = 0
		card={}
		num = int(input("请输入水果类型"))
		for temp in cards:
			if num == temp["num"]:
				flag = 1
				break
		if flag == 1:	
			print("水果已经存在已存在")
			continue
		chengzi = int(input("请输入橙子数量"))
		pingguo = int(input("请输入苹果数量"))
		xiangjiao = int(input("请输入香蕉数量"))
		xigua = int(input("请输入西瓜数量"))
		card["num"] = num
		card["chengzi"] = chengzi
		card["pingguo"] = pingguo
		card["xiangjiao"] = xiangjiao
		card["xigua"] = xigua
		cards.append(card)
		print("录入成功")
		for i in cards:
			print(i)
	elif a == 2:
		print("查看水果类型")
		num = int(input("请输入水果数量"))
		flag = 0
		for temp in cards:
			if num == temp["num"]:
				flag = 1
				print("水果是:%d\n橙子是:%s\n苹果是:%0.2f\n香蕉是:%0.2f\n西瓜是:%0.2f\n"%(card["num"],card["chengzi"],card["pingguo"],card["xiangjiao"],card["xigua"]))
				break
		if flag == 0:
			print("没有此类水果")
			continue
	elif a == 3:
		print("请输入你要修改的水果类型")
		num = int(input("请输入你要修改的水果数量"))
		for i in cards:
			if num == i["num"]:
				print("1:修改水果".center(30," "))
				print("2:修改橙子数量".center(30," "))
				print("3:修改苹果数量".center(32," "))
				print("4:修改香蕉数量".center(32," "))
				print("5:修改西瓜数量".center(32," "))
				f = int(input("请输入你要修改的选项:"))
				if f == 1:
					num = int(input("请输入水果类型"))
					i["num"] = num
				elif f == 2:
					chengzi = int(input("请输入橙子数量:"))
					i["chengzi"] = chengzi
				elif f == 3:
					pingguo = int(input("请输入苹果数量:"))
					i["pingguo"] = pingguo
				elif f == 4:
					xiangjiao = int(input("请输入香蕉数量:"))
					i["xiangjiao"] = xiangjiao
				elif f == 5:
					xigua = int(input("请输入西瓜数量:"))
					i["xigua"] = xigua
			else:
				print("没有此类水果")
	elif a == 4:
		num = int(input("请输入要去除的水果"))
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
			print("没有这类水果")
	elif a == 5:
		print("打印")
		print("水果\t橙子\t苹果\t香蕉\t西瓜\t")
		for i in cards:
			print("%d\t%s\t%0.2f\t%0.2f\t%0.2f\t"%(i["num"],i["chengzi"],i["pingguo"],i["xiangjiao"],i["xigua"]))
	elif a == 6:
		sure_num = int(input("1确认退出,0返回功能"))
		if sure_num == 0:
			print("退出成功")
			continue
		break



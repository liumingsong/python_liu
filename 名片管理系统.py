cards = []
print("欢迎来到名片系统".center(30,"*"))
print("1:添加名片".center(30," "))
print("2:查询名片".center(30," "))
print("3:修改名片".center(30," "))
print("4:删除名片".center(30," "))
print("5:打印名片".center(30," "))
print("6:退出系统".center(30," "))
def input_fun():
	while True:
		fun_num = int(input("请选择功能1:添加名片,2:查询名片,3:修改名片,4:删除名片,5:打印名片"))
		if fun_num == 1:
			add_card()
		elif fun_num == 2:
			find_card()
		elif fun_num == 3:
			update_card()
		elif fun_num == 4:
			del_num()
		elif fun_num == 5:
			all_card()
		else:
			break
def add_card():
	card = {}
	name = input("请输入名字")
	job = input("请输入职位")
	company = input("请输入公司")
	phone = int(input("请输入联系"))
	card["name"] = name
	card["job"] = job
	card["company"] = company
	card["phone"] = phone
	cards.append(card)
	print("添加成功")
	print(cards)
def find_card():
	name = input("请输入查找姓名")
	flag = 0
	for temp in cards:
		if name == temp["name"]:
			print("名字:%s\n工作:%s\n公司:%s\n电话:%s\n"%(temp["name"],temp["job"],temp["company"],temp["phone"]))
			flag = 1
	if flag == 0:
		print("查无此人")


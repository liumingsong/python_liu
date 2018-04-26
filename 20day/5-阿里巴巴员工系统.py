import time
from random import randint
list = []
def addUser():
	dict = {}
	name = input("请输入名字")
	job = input("请输入工作岗位")
	salary = float(input("请输入薪水"))
	create_time = randint(0,1524190943)
	dict["name"] = name
	dict["job"] = job
	dict["salary"] = salary
	dict["create_time"]  = create_time
	list.append(dict)
	print("添加成功")
def findUser():
	name = input("请输入名字")
	for temp in list:
		if name == temp["name"]:
			print("名字是:%s"%name)
			now = int(time.time())
			diff = now - temp["create_time"]
			day = diff / 86400
			print("薪水%f"%(temp["salary"]/30*day))
			break
def outCompany():
	name = input("请输入离职员工")
	flag = 0
	for temp in list:
		if name == temp["name"]:
			flag = 1
			sure_num = int(input("0确认删除,1返回功能"))
			if sure_num == 0:
				list.remove(temp)
				print("删除成功")
def showMenu():
	print("员工管理系统v1.0".center(20,"*"))
	print("1:员工入职")
	print("2:查找员工")
	print("3:员工离职")
def  fun_input():
	while True:
		showMenu()
		fun = int(input("请选择功能"))
		if fun == 1:
			addUser()
		elif fun == 2:
			findUser()
		elif fun == 3:
			outCompany()
fun_input()

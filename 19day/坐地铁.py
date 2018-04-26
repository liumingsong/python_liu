list=[]
allcount = 0
def sub_money(distance,count,month):
	info={}
	money = 0
	sum = 0
	global allcount
	allcount+=count*30
	for i in range(0,count*30):
		if distance <=6:
			money = 3
		elif 6 < distance and distance <= 12:
			money = 4
		elif 12 < distance and distance <= 22:
			moeny = 5
		elif 22 < distance and distance <= 32:
			money = 6
		elif distance > 32:
			if (distance-32)%20 == 0:
				money = 6 + (distance - 32) /20
			else:
				money = 6 + int((distance - 32) /20)+1
		if sum >=100 and sun < 150:
			money = money *0.8
		elif sum >= 150 and sum < 400:
			money = money *0.5
		sum +=money
	info[month]=sum
	list.append(info)
def sum_money():
	sum = 0
	for i in list:
		for i in list:
			for k,v in i.items():
				print("%d月份花了%0.2f元"%(k,v))
				sum+=v
	return sum
def user_input():
	loop = True
	while loop:
		mode = int(input("菜单 1:乘坐 2:计算\n"))
		if mode == 1:
			distance = float(input("请输入距离:"))
			month = int(input("请输入月份:"))
			count = int(input("请输入每天的次数："))
			if month >= 13 or month <1:
				print("输入的不合法")
			elif count<=8:
				print("输入的不合法")
			else:
				sub_money(distance,count,month)
		else:
			result = sum_money()
			print("总共花了%0.2f元,一共坐了%d次地铁"%(result,allcount))
			loop = False
user_input()

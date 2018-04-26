def aa(x,y,f):
	d = 0
	if f == "+":
		d = x+y
		print("和是%0.2f"%d)
	elif f == "-":
		d = x-y
		print("差是%0.2f"%d)
	elif f == "*":
		d = x*y
		print("积是%0.2f"%d)
	elif f == "/":
		if y != 0:
			d = x/y
			print("商是%0.2f"%d)
		else:
			print("输入有误")
while True:
	x = float(input("请输入一个数字"))
	y = float(input("请再输入一个数字"))
	f = input("请输入+,-,*,/")
	aa(x,y,f)

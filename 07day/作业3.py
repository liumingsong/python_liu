x = float(input("请输入一个数字"))
y = float(input("请再输入一个数字"))
aa = input("请输入+-*/")
if aa == "+":
	print(x+y)
elif aa == "-":
	print(x-y)
elif aa == "*":
	print(x*y)
elif aa == "/":
	print(x/y)
else:
	print("输入错误")

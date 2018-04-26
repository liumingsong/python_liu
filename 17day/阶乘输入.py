def a(num):
	if num == 1:
		return 1
	else:
		return num*a(num-1)
num = int(input("请输入数字:"))
a(num)
print(num*a(num-1))



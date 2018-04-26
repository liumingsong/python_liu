def a(s):
	if s%400 == 0 and s%4 == 0:
		print("%d是闰年"%s)
	elif s%100 != 0:
		print("%d是闰年"%s)
	else:
		print("%d是平年"%s)
while True:
	s = int(input("请输入年份"))
	a(s)

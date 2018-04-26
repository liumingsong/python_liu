h = []
def a():
	s = input("请输入一个英雄名字")
	h.append(s)
while True:
	a()
	if len(h) == 5:
		print(h)
		break


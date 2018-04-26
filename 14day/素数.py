def i(s,d):
	for i in range(s,d):
		flag = 0
		for f in range(s,i):
			if i % f == 0:
				flag =1
				break
		if flag == 0:
			print(i)
while True:
	s = int(input("请输入"))
	d = int(input("请再输入"))
	i(s,d)

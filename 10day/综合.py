a = []
s = []
d = 3
while d > 0:
	z = {}
	na = input("请输入名字")
	if na in s:
		print("名字已经有，请重新输入")
		continue;
	s.append(na)
	ag = int(input("请输入年龄"))
	se = input("请输入性别")
	qq = input('请输入QQ:')
	wi = int(input('请输入体重'))
	z["na"]=na
	z["se"]=se
	z["qq"]=qq
	z["wi"]=wi
	a.append(z)
	d = d-1;
for l in a:
	print(l)
#	for j,v ini.items():
#		print("%s:%s"%(j,v))
z = 0
for i in a:
	z+=i["年龄"]
print("平均年龄为%0.2f"%(z/len(a)))

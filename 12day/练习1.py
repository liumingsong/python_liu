a = []
c = []
s = 0
while True:
	if s == 3:
		break
	dict = {}
	na = input("请输入你的名字")
	age = int(input("请输入你的年龄"))
	sex = input("请输入你的性别")
	wei = float(input("请输入你的体重"))
	if na not in c:
		dict["na"] = na
		dict["age"] = age
		dict["sex"] = sex
		dict["wei"] = wei
		a.append(dict)
		c.append(na)
		print(a)
		s+=1
	else:
		print("名字已存在")
age_sum = 0
for i in a:
	age_sum = age_sum+i.get("age")
	print(i)
print("平均年龄是%0.2f"%(age_sum/len(a)))
for l in dict:
	print(l)

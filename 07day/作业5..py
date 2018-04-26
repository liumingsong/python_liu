hi = float(input("请输入身高"))
my = float(input("请输入身价"))
fe = float(input("请输入颜值"))
if hi > 180 and my > 1000000 and fe > 99:
	print("高富帅")
elif my > 1000000 and fe > 99:
	print("富帅")
elif fe > 99:
	print("帅")
elif hi < 160 and my < 100 and fe < 60:
	print("矮矬穷")

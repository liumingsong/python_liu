def c_p(p):
	if p.startswith("1") and len(p) == 11:
		return True
	else:
		return False
p = input("请输入手机号")
result = c_p(p)
if result == False:
	print("手机号错误的")
p2 = input("请输入手机号")
result = c_p(p2)
if result == False:
	print("手机号错误的")

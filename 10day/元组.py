a = ("laowang","laozhang","laosun","laoxue")
s = input("请输入一个名字")
if s in list(a):
	print("他在床头柜里面")
else:
	print("他跳窗跑了")
if s not in list(a):
	print("你王哥我不在")
else:
	print("老公，王哥在")

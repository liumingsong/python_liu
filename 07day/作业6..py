se = float(input("请输入你的身高"))
wt = float(input("请输入你的体重"))
a = (wt/(se*se))
if a < 18.5:
	print("过轻")
elif ((a > 18.5) and (a < 25)):
	print("正常")
elif ((a > 25) and (a < 28)):
	print("过重")
elif ((a >28) and (a < 32)):
	print("肥胖")
elif a > 32:
	print("严重肥胖")

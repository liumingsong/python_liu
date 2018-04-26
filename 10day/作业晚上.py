a = ['德玛西亚','无双剑姬','九八K','M4A1']
print(a)
for i in a:
	print('邀请%s来吃饭'%i)
print('*'*50)
print('%s因为拯救不能来啦'%a[3])
a[3] = '疾风剑豪'
print('*'*50)
for i in a:
	print('邀请%s来吃饭'%i)
print('*'*50)
print('我找到了更大的一张桌子，能再来三个人')
print('*'*50)
a.insert(0,'赵信')
a.insert(3,'小法')
a.append('剑圣')
print('邀请%s来吃饭'%i)
for i in a:
	print('邀请%s来吃饭'%a)
print('*'*50)
for i in range(len(a)):
	if len(a) == 2:
		break
	print('%s,餐桌没来，不能邀请你来了'%a[0:1])
	a.pop(0)
print('*'*50)
for i in a:
	print('%s,请及时来吃饭'%i)
print('共邀请了%d位嘉宾来吃饭'%len(a))
del a[0:5]
print(a)
print('*'*50)
print('共邀请了%d位嘉宾来吃饭'%len(a))
print('*'*50)
print(a)

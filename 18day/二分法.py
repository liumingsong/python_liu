list = [13,6,10,21,30,50,4,89,2]
key = 4
center = int(len(list)/2)
if key in list:
	while True:
		if list[center] > key:
			center = center - 1
		elif list[center] < key:
			center = center + 1
		elif list[center] == key:
			print("数值%d在索引%d的位置"%(key,center))
			break
else:
	print("没有该数字")


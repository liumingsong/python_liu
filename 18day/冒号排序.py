list = [13,6,10,21,30,50,4,89,2]
print(list)
for i in range(len(list)):
	for j in range(i+1,len(list)):
		if list[i]>list[j]:
			list[i],list[j] = list[j],list[i]
	print(list)
#a = list
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


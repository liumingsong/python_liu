list = [{"beijing":{"mianji":1290,"remkou":123123},"shanghai":{"mianji":12331,"renkou":123123}}]
def xxx():
	for i in list:
		for h in i.keys():
			for k in i[h].keys():
				print(h,k,i[h][k])
for i in range(100):
	xxx()

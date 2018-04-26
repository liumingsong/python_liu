cards = [{"name":"尹天","age":20},{"name":"豪哥","age":22},{"name":"崔健","age":18}]
for i in cards:
	print(i)
	for k,v in i.items():
	#print(i)001
	#print(cards.get(i))
		print("%s的值是%s"%(k,v))

def sum_find(a,b,*args,**kwargs):
	c = a+b
	sum_find+=c
	for i in args:
		sum_find+=i
		print(i)
		for i in kwargs:
			sum_find+=i
			print(i)
sum_find(1,2,3,4,5,6,7,"age"=12)

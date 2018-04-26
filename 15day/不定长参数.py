def sum(a,b,*args,**kwargs):
	c = a+b
	print(a)
	print(b)
	print(args)
	print(kwargs)
	return c
print(sum(1,2,3,4,5,6,7,8,9,age=22))

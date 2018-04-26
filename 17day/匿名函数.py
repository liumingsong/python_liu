list = lambda x,y:x+y


print(list(1,2))


stus = [{"name":"laowang","age":19},{"name":"song","age":14}]
stus.sort(key = lambda y:y["name"])
print(stus)

def sun(a,b,args):
	print(args(a,b))
sun(1,2,lambda a,b:a*b)


def su(a,b,c=3,*args,**kwargs):
	print(a)
	print(b)
	print(args)
	print(kwargs)
su(1,2,3,4,5,6,age=12)







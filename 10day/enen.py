a = [1,2,3,4,5,6,7]
for i in a[:]:
	a.remove(i)
print(a)
a = [1,2,3,4,5,6,7]
for i in range(len(a)-1,-1,-1):
	a.pop(i)
	print(a)
print(a)

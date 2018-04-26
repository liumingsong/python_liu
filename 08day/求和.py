i = 0
my_sum = 0
while i <= 100:
	my_sum+=i
	print(i)
	if my_sum%2 == 0:
		print("%d是偶数"%my_sum)
	if my_sum%2 == 1:
		print("%d是奇数"%my_sum)
	i+=2

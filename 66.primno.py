num = int(input())
 
for i in range(2, int(num/2)):
	if num % i  == 0:
		print("no")
		break
else:
	print("yes")

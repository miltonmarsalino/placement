a=0
b=1
n=int(input())
ans=[1]
for i in range(n):
	s=a+b
	a=b
	b=s
	ans.append(s)
for i in range(n):
	print(ans[i],end=" ")

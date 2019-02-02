n = int(input())
a = list(map(int,input().split()))
m1 = a[0]
for i in range (n):
if a[i]<m1:
m1 = a[i]
m2 = max(a)
print(m2 , m1)

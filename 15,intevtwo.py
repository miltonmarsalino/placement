# even numbers between two interval
n,m = map(int,input().split())
for num in range(n+1, m ): 
      
    
    if num % 2 == 0: 
        print(num, end = " ") 

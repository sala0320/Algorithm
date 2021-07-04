n = int(input())
count = 0
if n == 1 or n == 3:
    count = -1
elif n % 5 == 1 or n % 5 == 3:
    count = (n//5-1) + (n-((n//5-1)*5))//2 
else:
    count = (n // 5) + (n % 5) // 2
print(count)

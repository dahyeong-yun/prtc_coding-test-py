n = int(input())
bag = 0

while n % 5 > 0:
    n -= 3
    bag += 1

if n < 0:
    print(-1)
else:
    print(n // 5 + bag)

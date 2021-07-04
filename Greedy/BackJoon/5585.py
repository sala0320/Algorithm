n = int(input())
coin_type = [500, 100, 50, 10, 5, 1]
count = 0

change = 1000 - n
for coin in coin_type:
    count += change // coin
    change %= coin

print(count)
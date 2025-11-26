
n = int(input("Enter the original number of coins: "))
coins = list(map(int, input("Enter the coins: ").split()))

coin_count = {}

for coin in coins:
    coin_count[coin] = coin_count.get(coin, 0) + 1

missing_coin = None
for coin, count in coin_count.items():
    if count % 2 != 0:  
        missing_coin = coin
        break

print("The missing coin number is:", missing_coin)
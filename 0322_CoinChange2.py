# 貪欲法（参考）

def coin_change_greedy(coins, amount):

    coins.sort(reverse=True)

    count = 0

    for coin in coins:
        if amount == 0:
            break
        count += amount // coin
        amount %= coin

    return count if amount == 0 else -1


coins = [1, 2, 5]
amount = 11
print(coin_change_greedy(coins, amount))

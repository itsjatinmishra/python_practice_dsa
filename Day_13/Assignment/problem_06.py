def change(coins, target):
    coins.sort()
    i = len(coins) - 1
    count = 0

    while target > 0:
        if target - coins[i] < 0:
            i -= 1
        else:
            target = target - coins[i]
            count += 1

    return count


target = 11
coins = [1,2,7]

print(change(coins, target))

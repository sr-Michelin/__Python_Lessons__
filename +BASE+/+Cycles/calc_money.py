ti = 5
found_coins = 14990
ad_coins = 1660
ad_coins_ex = 1050*4
used_coins = 3000
coins = found_coins

# print(found_coins+ti*(ad_coins_from_work+ad_coins-used_coins))

for i in range(0, ti):
    coins = coins + ad_coins + ad_coins_ex - used_coins
    print('Місяць {0}, {1} гривень. '.format(i + 1, coins))


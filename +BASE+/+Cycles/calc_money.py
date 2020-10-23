found_coins = 9300
ad_coins = 1660
ad_coins_ex = 4200
used_coins = 1700
coins = found_coins
ti = 3

# print(found_coins+ti*(ad_coins_from_work+ad_coins-used_coins))

for i in range(0, ti):
    coins = coins + ad_coins + ad_coins_ex - used_coins
    print('Місяць {0}, {1} гривень. '.format(i + 1, coins))
    # print('Місяць %s, %s гривень.' %(i+1,coins))

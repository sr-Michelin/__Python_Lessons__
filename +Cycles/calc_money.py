'''lst1 = list(range(0,5))
lst2 = ['M','i','k','e']

n =  max(len(lst2),len(lst1))

for i in lst1:
    for j in lst2:
        print('',i,j,end=' ')

print('\t')
for i in range(0,n):
    for j in range(0,n):
        print('',i,j,end=' ')'''


found_coins = 0
ad_coins = 1800
ad_coins_from_work = 5000
used_coins = 1500
coins = found_coins
ti = 12

# print(found_coins+ti*(ad_coins_from_work+ad_coins-used_coins))

for i in range(0,ti):
    coins = coins+ad_coins+ad_coins_from_work-used_coins
    print('Місяць {0}, {1} гривень. '.format(i+1, coins))
    print('Місяць %s, %s гривень.' %(i+1,coins))
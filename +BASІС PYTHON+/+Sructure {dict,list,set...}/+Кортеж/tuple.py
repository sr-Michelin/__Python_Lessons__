import math

fzf_41 = ('Vasyl_Polcanov', 'Krystyna_Kovach', 'Mike_Tonne', 'Ilya_Shvaga',
          'Lybomyr_Probytyj-Sosok', 'Romchyk_Bukhach-Kyrylyk', 'Alonya_Nicolayeva')
fzf_42 = ('Mike_Shevchenko', 'Denys_Ohrymovich', 'Yara_Ostapchuk')

print('{0} students from old fzf_41: '.format(len(fzf_41)), end='')
for i in fzf_41:
    print(i, end=';  ')

print('\n{0} students from old fzf_42: '.format(len(fzf_42)), end='')
for i in fzf_42:
    print(i, end=';  ')

fzf_51 = fzf_41 + fzf_42
print('\n{0} students from fzf_51: '.format(len(fzf_51)), end='')
for i in fzf_51:
    print(i, end=';  ')

lucky_man = math.floor((len(fzf_51) + 10) * 0.4 - 1)
print('\nCount of "lucky man" from  fzf_51: ', lucky_man)

fzf_42.index('Mike_Shevchenko', 0, 3)  # пошук за значенням у певних межах (тут 0-3)

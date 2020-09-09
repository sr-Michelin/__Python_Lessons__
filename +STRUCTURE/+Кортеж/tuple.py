import math

fzf_41 = ('Vasyl_Polcanov', 'Krystyna_Kovach','Mike_Tonne', 'Ilya_Kosyak-Shvaga', 'Lybomyr_Probytyj-Sosok', 'Romchyk_Bukhach-Kyrylyk','Alonya_Anime-Nicolayeva')
print('Count of group fzf_41: ',len(fzf_41))
print('fzf_41: ',fzf_41)



fzf_51 = ('sr. Mike_Shevchenko','Denys_Ohrymovich','Yartna_Ostapchuk',fzf_41)

print('')
print('New students: ',end=' ')

for i in range(3):
    print('',fzf_51[i],end=',')
    i+=1

print('\nfzf_51: ',fzf_51)
lucky_man = math.floor(int(len(fzf_51)-1+len(fzf_41)+12)*0.4)
print('Count of group fzf_51: ',len(fzf_51)-1+len(fzf_41))
print('Count of "lucky man" fzf_51: ',lucky_man)


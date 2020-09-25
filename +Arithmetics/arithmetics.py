a=5;b=3;c=True;d=False;
print('a=',a,',b=',b,',c=',c,',d=',d)
print('a+b=',a+b)   # Ясно
print('a-b=',a-b)   # Ясно
print('a*b=',a*b)   # Ясно
print('a**b=',a**b) # Ясно

print('a/b=',a/b)   # Остача від ділення
print('a%b=',a%b)   # Ціла частина ділення

print('a<<b=',a<<b) # Зсуває біти чисел вправо
print('a>>b=',a>>b) # Зсуває біти чисел вліво

print('a&b=',a&b) # Побітова оперпція 'І' над числами
print('a|b=',a|b) # Побітова оперпція 'АБО' над числами
print('a^b=',a^b) # Побітова оперпція 'ВИКЛЮЧНО' над числами
print('a~=',~a)   # Побітова оперпція 'НЕ' над числами --> -(x+1)

print('a>b,  тому ', a>b, end= ' ::: ')
print('a<b,  тому ', a<b) # Логічні операції '>' i '<'
print('a>=b, тому ',a>=b, end= " ::: ")
print('a<=b, тому ',a<=b) # Логічні операції '>=' i '<='
print(a==b, ', a==b',end=" ::: ")
print(a!=b, ', a!=b')     # Логічні операції '==' i '!='

print(not c, 'not c - not True')                  # NOT
print(c and d,', бо True AND False = False')      # AND
print(c or d, ', між True і False вибирає True')  # OR


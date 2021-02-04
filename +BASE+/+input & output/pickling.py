# Довгострокове збереження даних у форматі .data - концервація, і подальше відтворення через load - розконцервацію
# wb - бінарний запис


import pickle

shoplist_file = 'shoplist.data'

shoplist = ['хліб', 'мазік', 'помідори', 'цибуля', 'банани', 'печиво "Вушка"', 'апельсин', ]  # хана фігурі

f = open(shoplist_file, 'wb')
pickle.dump(shoplist, f)  # помещаем объект в файл
f.close()

del shoplist

f = open(shoplist_file, 'rb')
storedlist = pickle.load(f)  # загружаем объект из файла
print(storedlist)

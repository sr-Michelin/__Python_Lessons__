# filter - фільтр за параметрами
# у даному випадку фільтрація за парними числами

a = list(range(10))
b = list(filter(lambda x: not x % 2, a))
print(b)

print(list(filter(lambda x: not x % 2, list(range(10)))))  # запис еквівалентий до попереднього


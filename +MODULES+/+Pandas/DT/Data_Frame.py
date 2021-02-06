import pandas as pd

"""DataFrame --- повноцінна таблиця із множино рядків та стовпців"""
df_0 = pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
# index - список міток для записів (імена рядків)
# columns - список міток для записів (імена стовпців)
# copy - при True створюється копія масиву даних

df_1 = pd.DataFrame({'name': ['M', 'Y', 'K', 'Sh'], 'course': [5] * 4}, copy=True)  # зі словника
df_1cl = df_1.columns  # columns

# -----------------
import numpy as np

d2 = {'price': np.array([1, 2, 3]), 'count': np.array([10, 23, 13])}
df_2 = pd.DataFrame(d2, index=['A', 'B', 'C'])  # використання numpy

# -----------------
d3 = [{'price': [1, 2, 3], 'count': [11, 12, 13]}, {'price': [4, 5, 6], 'count': [14, 15, 16]}]
df_3 = pd.DataFrame(d3)  # через множину словників
# print(df_3.info())  # повна інформація про таблицю

# -----------------
d4 = np.array([[1, 2, 3], [1, 2, 3]])
df_4 = pd.DataFrame(d4)  # з двохвимірного масиву (матриці numpy)

"""Робота з Data_Frame:"""
d5 = df_2['price']  # вибір стовпця ---> Series
d6 = df_2[0:2]  # зріз по рядкам ---> Data_Frame

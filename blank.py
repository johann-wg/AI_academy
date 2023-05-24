import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('한국가스공사_천연가스.csv',encoding='cp949')
dff = df.drop(df.columns[1], axis=1)
plt.bar(dff.iloc[1:,0],dff.iloc[1:,1])

# plt.axis([-4.05, 85.05, -281199.85000000003, 5949548.85])

x_range, y_range = plt.xlim(), plt.ylim()
print(x_range, y_range)

# axis_range = plt.axis('scaled')
# print(axis_range)


plt.show()
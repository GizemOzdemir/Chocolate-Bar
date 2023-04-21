# -*- coding: utf-8 -*-
"""Chocolate Bar

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uBzlRd0qLt8lwm7VMEC1A4QwsYuwBHrJ
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_=pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2022/2022-01-18/chocolate.csv")

df=df_.copy()

df.head()

df.info

df.shape

df.describe().T

df.isnull().sum()

df.dtypes

df['cocoa_percent']=df['cocoa_percent'].str.replace('%','').astype(float)/100

df.dtypes

df.head()

"""**YILLARA GÖRE KAKAO YÜZDELERİ**

"""

df_year_cocoa = df.groupby('review_date').aggregate({'cocoa_percent':'mean'})

df_year_cocoa

df_year_cocoa=df_year_cocoa.reset_index()

sns.set()
plt.figure(figsize=(10, 3))
ax = sns.lineplot(x='review_date', y='cocoa_percent', data=df_year_cocoa)
ax.set(xticks=df_year_cocoa.review_date.values)
plt.xlabel("Yıllar")
plt.ylabel("Ortalama Kakao Yüzdeleri")
plt.title("Yıllara Göre Ortalama Kakao Yüzdeleri\n")
plt.show()

"""**YILLARA GÖRE RATİNG DEĞERLERİNİN DEĞİŞİMİ**"""

df_year_rating = df.groupby('review_date').aggregate({'rating':'mean'})

df_year_rating=df_year_rating.reset_index()

sns.set()
plt.figure(figsize=(10, 3))
ax = sns.lineplot(x='review_date', y='rating', data=df_year_rating)
ax.set(xticks=df_year_rating.review_date.values)
plt.xlabel("Yıllar")
plt.ylabel("Ortalama Rating Değerleri")
plt.title("Yıllara Göre Ortalama Rating Değerleri\n")
plt.show()

"""**KAKAO DEĞERLERİ VE RATİNG ARASINDAKİ İLİŞKİ**"""

sns.jointplot(x = "rating", y = "cocoa_percent",
              kind = "reg", 
              data = df,
              palette='set2',
              dropna = True)
plt.xlabel("Rating Değerleri")
plt.ylabel("Kakao Yüzdeleri")

g = sns.catplot(x="cocoa_percent", y="review_date",
                hue="rating",aspect=3,
                data=df).set_xticklabels(rotation=90)
plt.xlabel("Kakao Yüzdeleri")
plt.ylabel("Yıllar")
plt.title("Yıllara Göre Kakao Yüzdeleri ve Rating Değerleri Arasındaki İlişki")

"""**RATİNG DEĞERLERİNE GÖRE ÇİKOLATALARIN KATEGORİLERE AYRILMASI**"""

tatmin_edici_olmayan= df[df['rating'] < 3.0]
tatmin_edici=df[(df['rating'] >= 3.0) & (df['rating'] < 4.0)]
çok_begenilen=df[df['rating'] >= 4.0]

baslık_isimleri= ['Tatmin Edici Olmayanlar', 'Tatmin Edici Olanlar','Çok Beğenilenler']

sizes = [tatmin_edici_olmayan.shape[0],tatmin_edici.shape[0],çok_begenilen.shape[0]]

colors = ['#FF0000','#FFFF00','#FFA500']

explode = (0.05,0.05,0.05)

plt.pie(sizes, colors=colors, labels=baslık_isimleri,
        autopct='%1.1f%%', pctdistance=0.85,startangle=90,
        explode=explode)
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('Çikolata Barların Beğenilme Oranları')
plt.show()
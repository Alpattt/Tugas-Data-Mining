# -*- coding: utf-8 -*-
"""Selamat Datang di Colaboratory

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

# Maliki Alfath (4101421080)

#Memuat data
import pandas as pd

# Membaca dataset yang upload
df = pd.read_csv('movie_sample_dataset.csv')

#Menampilkan beberapa baris pertama dari dataset.
df.head()

import numpy as np
#Ganti ? dengan NaN
df.replace("?", np.nan, inplace=True)

#Memeriksa jumlah missing value di setiap kolom
print(df.isnull().sum())

#cek tipe data
df.dtypes

# Menghapus baris yang memiliki nilai kosong di kolom gross dan budget.
cleaning = df.dropna(subset=['gross', 'budget','color','genres','director_name'])

#str.capitalize() digunakan untuk mengubah huruf pertama menjadi kapital agar konsisten antara "Color" dan "color".
cleaning['actors'] = cleaning['actors'].str.capitalize()

# Hitung rata-rata gross dan budget dan mengisi sel kosong dengan rata-rata
colsToReplace = ['gross', 'budget']
for col in colsToReplace:
  avg_value=df[col].astype(float).mean()
  df[col].replace(np.nan, avg_value, inplace=True)
  print(f"Average of {col}: {avg_value}")

# Mencari modus (nilai yang sering muncul) pada kolom director_name, color, genres
cekmodusdirector=df["director_name"].value_counts().idxmax()
cekmoduscolor=df["color"].value_counts().idxmax()
cekmodusgenres=df["genres"].value_counts().idxmax()
# mengisi sel kosong nilai modus
df["director_name"].replace(np.nan,cekmodusdirector , inplace=True)
df["color"].replace(np.nan,cekmoduscolor , inplace=True)
df["genres"].replace(np.nan,cekmodusgenres , inplace=True)
# mengecek modus director, color, dan genres
print(f"Nilai yang sering muncul di kolom director = {cekmodusdirector}")
print(f"Nilai yang sering muncul di kolom color = {cekmoduscolor}")
print(f"Nilai yang sering muncul di kolom genres = {cekmodusgenres}")

# Membuat cleaning sebagai salinan dari DataFrame asli (df)
cleaning = df.copy()

# Menghapus baris yang memiliki NaN di kolom gross dan budget
cleaning = cleaning.dropna(subset=['gross', 'budget'])

# Filter baris dengan nilai budget dan gross yang bernilai negatif
cleaning = cleaning[(cleaning['gross'] >= 0) & (cleaning['budget'] >= 0)]

# Filter baris dengan nilai duration dan imdb score yang bernilai negatif
cleaning = cleaning[(cleaning['duration'] >= 0) & (cleaning['imdb_score'] >= 0)]

print(df.isnull().sum())

# Mengubah tipe data kolom yang diperlukan
df[["color", "director_name", "genres"]]=df[["color", "director_name", "genres"]].astype(str)
df[["budget", "gross"]]=df[["budget", "gross"]].astype(float)

# Normalisasi teks ke huruf kecil
cleaning['color'] = cleaning['color'].str.lower()
cleaning['director_name'] = cleaning['director_name'].str.lower()
cleaning['genres'] = cleaning['genres'].str.lower()
cleaning['language'] = cleaning['language'].str.lower()
cleaning['country'] = cleaning['country'].str.lower()
cleaning['actors'] = cleaning['actors'].str.lower()

# Untuk cek data-data apakah sudah menjadi huruf kecil atau belum
print(cleaning['actors'].head())

# Menyimpan data yang telah diproses ke dalam file CSV baru
cleaning.to_csv('movie_dataset_cleaned.csv', index=False)
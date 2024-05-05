# Simple Big Data Analysis | X-Projetion
import pandas as pd
import matplotlib.pyplot as plt

# Baca file CSV ke dalam DataFrame
df = pd.read_csv('big_data.csv')

# Tampilkan informasi singkat tentang DataFrame
print("Informasi tentang DataFrame:")
print(df.info())

# Tampilkan lima baris pertama dari DataFrame
print("\nLima baris pertama dari DataFrame:")
print(df.head())

# Lakukan analisis sederhana
print("\nStatistik Deskriptif:")
print(df.describe())

# Lakukan analisis lebih lanjut
# Misalnya, hitung jumlah data unik dalam kolom tertentu
unique_values = df['nama'].nunique()
print(f"\nJumlah data unik dalam kolom 'nama': {unique_values}")

# Lakukan visualisasi data jika perlu
# Contoh: Histogram dari kolom tertentu
df['usia'].hist()
plt.title('Histogram of usia')
plt.xlabel('Usia')
plt.ylabel('Frekuensi')
plt.show()

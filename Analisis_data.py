# import numpy as np
# import matplotlib.pyplot as plt
# import csv
# from collections import Counter

# # Variables para almacenar los datos
# ratings = []
# reviews = []
# installs = []
# genres = []  # Lista para almacenar todos los géneros

# # Leer el archivo CSV y almacenar solo las filas válidas
# with open('Play_Store_Data.csv', 'r', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     header = next(reader)  # Leer y descartar el encabezado
#     for row in reader:
#         # Validar filas con exactamente 13 columnas antes de procesarlas
#         if len(row) == 13:
#             try:
#                 rating = float(row[2])  # Columna de Ratings
#                 review = float(row[3])  # Columna de Reviews
#                 install = int(row[5].replace('+', '').replace(',', ''))  # Columna de Installs
#                 genre = row[1]  # Columna de Género

#                 # Agregar los valores a las listas correspondientes
#                 ratings.append(rating)
#                 reviews.append(review)
#                 installs.append(install)
#                 genres.append(genre)  # Agregar cada género a la lista de géneros

#             except ValueError:
#                 # Ignorar filas con datos no convertibles
#                 continue

# # Convertir listas a arrays de numpy
# ratings = np.array(ratings)
# reviews = np.array(reviews)
# installs = np.array(installs)

# # Contar las categorías de instalaciones para el gráfico de torta
# install_categories = ['0-10K', '10K-100K', '100K-1M', '1M-10M', '10M+']
# install_counts = [0, 0, 0, 0, 0]

# # Clasificar las instalaciones en categorías
# for install in installs:
#     if install < 10000:
#         install_counts[0] += 1
#     elif install < 100000:
#         install_counts[1] += 1
#     elif install < 1000000:
#         install_counts[2] += 1
#     elif install < 10000000:
#         install_counts[3] += 1
#     else:
#         install_counts[4] += 1

# # Contar géneros para el gráfico de barras
# genre_counts = Counter(genres)  # Conteo a partir de la lista de géneros
# genres_list = list(genre_counts.keys())
# genres_count = list(genre_counts.values())

# # Crear gráficos
# plt.figure(figsize=(12, 5))

# # Gráfico 1: Distribución de instalaciones (Gráfico de Torta)
# plt.subplot(1, 2, 1)
# plt.pie(install_counts, labels=install_categories, autopct='%1.1f%%', startangle=140)
# plt.title('Distribución de Instalaciones de las Aplicaciones')

# # Gráfico 2: Cantidad de aplicaciones por género (Gráfico de Barras)
# plt.subplot(1, 2, 2)
# plt.barh(genres_list, genres_count, color='green')
# plt.xlabel('Cantidad de Aplicaciones')
# plt.title('Cantidad de Aplicaciones por Género')

# # Mostrar los gráficos
# plt.tight_layout()
# plt.show()



# #GRAFICO 3

# # Variables para almacenar los datos
# total_reviews = 0
# total_installs = 0

# # Leer el archivo CSV y almacenar solo las filas válidas
# with open('Play_Store_Data.csv', 'r', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     header = next(reader)  # Leer y descartar el encabezado
#     for row in reader:
#         # Validar filas con exactamente 13 columnas antes de procesarlas
#         if len(row) == 13:
#             try:
#                 review = float(row[3])  # Columna de Reviews
#                 install = int(row[5].replace('+', '').replace(',', ''))  # Columna de Installs

#                 # Sumar los valores a los totales
#                 total_reviews += review
#                 total_installs += install

#             except ValueError:
#                 # Ignorar filas con datos no convertibles
#                 continue

# # Crear gráfico de torta
# labels = ['Total Reviews', 'Total Installs']
# sizes = [total_reviews, total_installs]
# colors = ['lightblue', 'lightgreen']
# explode = (0.1, 0)  # "explosion" para resaltar el primer segmento

# plt.figure(figsize=(8, 8))
# plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
# plt.title('Proporción de Total de Reviews e Instalaciones')
# plt.axis('equal')  # Igualar el aspecto de la torta
# plt.show()





# #GRAFICO 4

# # Variables para almacenar los ratings
# ratings = []

# # Leer el archivo CSV y almacenar solo las filas válidas
# with open('Play_Store_Data.csv', 'r', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     header = next(reader)  # Leer y descartar el encabezado
#     for row in reader:
#         # Validar filas con exactamente 13 columnas antes de procesarlas
#         if len(row) == 13:
#             try:
#                 rating = float(row[2])  # Columna de Ratings
#                 ratings.append(rating)  # Agregar el rating a la lista

#             except ValueError:
#                 # Ignorar filas con datos no convertibles
#                 continue

# # Definir los rangos de ratings
# bins = np.arange(1, 6, 1)  # Rango de 1 a 5 con intervalos de 1
# labels = ['1-2', '2-3', '3-4', '4-5']

# # Contar las aplicaciones en cada rango
# rating_counts, _ = np.histogram(ratings, bins=bins)

# # Crear gráfico de barras
# plt.figure(figsize=(10, 6))
# plt.bar(labels, rating_counts, color='skyblue')
# plt.xlabel('Rango de Ratings')
# plt.ylabel('Cantidad de Aplicaciones')
# plt.title('Distribución de Ratings de Aplicaciones')
# plt.xticks(rotation=45)  # Rotar etiquetas del eje x
# plt.tight_layout()  # Ajustar el layout
# plt.show()



import numpy as np
import matplotlib.pyplot as plt
import csv

# Variables para almacenar los datos
ratings = []
is_free = []  # Lista para indicar si la aplicación es gratuita o de pago

# Leer el archivo CSV y almacenar solo las filas válidas
with open('Play_Store_Data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)  # Leer y descartar el encabezado
    for row in reader:
        # Validar filas con exactamente 13 columnas antes de procesarlas
        if len(row) == 13:
            try:
                rating = float(row[2])  # Columna de Ratings
                price = row[4].strip()  # Columna de Precio

                # Determinar si la aplicación es gratuita o de pago
                is_free.append(price == '0' or price.lower() == 'free')
                ratings.append(rating)

            except ValueError:
                # Ignorar filas con datos no convertibles
                continue

# Definir rangos de ratings
rating_ranges = [(1, 2), (2, 3), (3, 4), (4, 5)]
range_labels = ['1-2', '2-3', '3-4', '4-5']

# Crear sets para aplicaciones en cada rango
free_set_1_2 = set()
free_set_2_3 = set()
free_set_3_4 = set()
free_set_4_5 = set()

paid_set_1_2 = set()
paid_set_2_3 = set()
paid_set_3_4 = set()
paid_set_4_5 = set()

# Clasificar aplicaciones en sets según su rango de ratings
for rating, free in zip(ratings, is_free):
    if 1 <= rating < 2:
        if free:
            free_set_1_2.add(rating)
        else:
            paid_set_1_2.add(rating)
    elif 2 <= rating < 3:
        if free:
            free_set_2_3.add(rating)
        else:
            paid_set_2_3.add(rating)
    elif 3 <= rating < 4:
        if free:
            free_set_3_4.add(rating)
        else:
            paid_set_3_4.add(rating)
    elif 4 <= rating <= 5:
        if free:
            free_set_4_5.add(rating)
        else:
            paid_set_4_5.add(rating)

# Contar aplicaciones únicas en cada rango
free_counts_list = [
    len(free_set_1_2), len(free_set_2_3), len(free_set_3_4), len(free_set_4_5)
]
paid_counts_list = [
    len(paid_set_1_2), len(paid_set_2_3), len(paid_set_3_4), len(paid_set_4_5)
]

# Crear gráfico de barras
bar_width = 0.35
x = np.arange(len(rating_ranges))

plt.bar(x - bar_width / 2, free_counts_list, bar_width, label='Gratuitas', color='skyblue')
plt.bar(x + bar_width / 2, paid_counts_list, bar_width, label='De Pago', color='salmon')

plt.xlabel('Rango de Ratings')
plt.ylabel('Cantidad de Aplicaciones')
plt.title('Cantidad de Aplicaciones por Rango de Ratings')
plt.xticks(x, range_labels)
plt.legend()
plt.tight_layout()

# Mostrar el gráfico
plt.show()

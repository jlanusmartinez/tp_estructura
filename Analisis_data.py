# Importación de bibliotecas necesarias
import numpy as np  # Para trabajar con arrays y operaciones numéricas
import matplotlib.pyplot as plt  # Para crear gráficos
import csv  # Para leer y escribir archivos CSV
from collections import Counter  # Para contar elementos en colecciones (aunque no se usa directamente en este código)

# Variables para almacenar los datos
ratings = []  # Lista para almacenar los ratings de las aplicaciones
reviews = []  # Lista para almacenar el número de reseñas de las aplicaciones
installs = []  # Lista para almacenar las instalaciones de las aplicaciones
genres = []  # Lista para almacenar los géneros de las aplicaciones

# Leer el archivo CSV y almacenar solo las filas válidas
with open('Play_Store_Data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)  # Crear un lector de CSV
    header = next(reader)  # Leer y descartar el encabezado
    for row in reader:  # Iterar sobre las filas del archivo
        if len(row) == 13:  # Comprobar que la fila tiene 13 columnas (válida)
            try:
                # Extraer y convertir los valores relevantes de cada fila
                rating = float(row[2])  # Convertir la calificación (rating) a float
                review = float(row[3])  # Convertir el número de reseñas (reviews) a float
                install = int(row[5].replace('+', '').replace(',', ''))  # Convertir las instalaciones a entero, limpiando caracteres no numéricos
                genre = row[1]  # Obtener el género de la aplicación
                # Añadir los valores a las listas correspondientes
                ratings.append(rating)
                reviews.append(review)
                installs.append(install)
                genres.append(genre)
            except ValueError:
                continue  # Si hay un error en la conversión, se ignora esa fila

# Convertir listas a arrays de numpy para una mayor eficiencia en cálculos y operaciones
ratings = np.array(ratings)
reviews = np.array(reviews)
installs = np.array(installs)

# Usar sets para eliminar duplicados de géneros
unique_genres = set(genres)  # Convierte la lista de géneros a un conjunto (set) para obtener valores únicos
# Contamos cuántas veces aparece cada género en la lista original
genre_counts = {genre: genres.count(genre) for genre in unique_genres}

# Convertir los géneros y sus respectivas cuentas a listas
genres_list = list(genre_counts.keys())
genres_count = list(genre_counts.values())

# Ordenar los géneros por la cantidad de aplicaciones en cada uno, de menor a mayor
sorted_genre_counts = sorted(zip(genres_count, genres_list))
genres_count_sorted, genres_list_sorted = zip(*sorted_genre_counts)

# Crear gráficos separados con el mismo tamaño de figura

# Gráfico 1: Distribución de instalaciones de las aplicaciones
plt.figure(figsize=(10, 6))  # Ajustar el tamaño del gráfico
install_categories = ['0-10K', '10K-100K', '100K-1M', '1M-10M', '10M+']  # Categorías de rangos de instalaciones
install_counts = [0, 0, 0, 0, 0]  # Inicializar contadores de aplicaciones para cada categoría

# Contamos las aplicaciones que caen en cada categoría de instalaciones
for install in installs:
    if install < 10000:
        install_counts[0] += 1
    elif install < 100000:
        install_counts[1] += 1
    elif install < 1000000:
        install_counts[2] += 1
    elif install < 10000000:
        install_counts[3] += 1
    else:
        install_counts[4] += 1

# Graficar la distribución de instalaciones
plt.bar(install_categories, install_counts, color='skyblue')
plt.xlabel('Categorías de Instalación')  # Etiqueta del eje X
plt.ylabel('Cantidad de Aplicaciones')  # Etiqueta del eje Y
plt.title('Distribución de Instalaciones de las Aplicaciones')  # Título del gráfico
plt.xticks(fontsize=10)  # Cambiar el tamaño de la fuente de las etiquetas en el eje X
plt.tight_layout()  # Ajustar el diseño para evitar que los elementos se solapen
plt.show()  # Mostrar el gráfico

# Gráfico 2: Cantidad de aplicaciones por género (ordenado de menor a mayor cantidad)
plt.figure(figsize=(10, 6))  # Ajustar el tamaño del gráfico
plt.barh(genres_list_sorted, genres_count_sorted, color='green')  # Crear un gráfico de barras horizontal
plt.xlabel('Cantidad de Aplicaciones')  # Etiqueta del eje X
plt.title('Cantidad de Aplicaciones por Género (Ordenado)')  # Título del gráfico
plt.yticks(fontsize=8)  # Cambiar el tamaño de la fuente de las etiquetas en el eje Y
plt.tight_layout()  # Ajustar el diseño
plt.show()  # Mostrar el gráfico

# Gráfico 3: Distribución de Ratings de Aplicaciones
ratings = []  # Reiniciar la lista de ratings

# Leer el archivo CSV nuevamente para obtener solo los ratings
with open('Play_Store_Data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)  # Leer y descartar el encabezado
    for row in reader:
        if len(row) == 13:  # Comprobar que la fila tiene 13 columnas (válida)
            try:
                rating = float(row[2])  # Obtener y convertir la calificación (rating)
                ratings.append(rating)  # Agregar el rating a la lista
            except ValueError:
                continue  # Si no se puede convertir el rating, se ignora esa fila

# Definir los rangos de ratings para el histograma
bins = np.arange(1, 6, 1)  # Rango de 1 a 5 con intervalos de 1
labels = ['[1-2)', '[2-3)', '[3-4)', '[4-5)']  # Etiquetas de los rangos

# Usar set para eliminar valores duplicados de los ratings antes de contar
unique_ratings = set(ratings)  # Convierte la lista de ratings a un conjunto para obtener valores únicos
rating_counts, _ = np.histogram(list(unique_ratings), bins=bins)  # Crear el histograma

# Crear gráfico de barras para la distribución de ratings
plt.figure(figsize=(10, 6))  # Ajustar el tamaño del gráfico
plt.bar(labels, rating_counts, color='skyblue')  # Graficar las barras
plt.xlabel('Rango de Ratings')  # Etiqueta del eje X
plt.ylabel('Cantidad de Aplicaciones')  # Etiqueta del eje Y
plt.title('Distribución de Ratings de Aplicaciones')  # Título del gráfico
plt.xticks(rotation=45)  # Rotar las etiquetas en el eje X para una mejor legibilidad
plt.tight_layout()  # Ajustar el diseño
plt.show()  # Mostrar el gráfico

# Gráfico 4: Distribución de aplicaciones por tipo (Pago o Gratuita)
tipo_traduccion = {
    "free": "Gratuita",  # Traducción de "free" a "Gratuita"
    "paid": "Pago"  # Traducción de "paid" a "Pago"
}

# Mapeo de categorías en inglés a español para géneros
genero_traduccion = {
    "teen": "Adolescente",
    "everyone": "Para todos",
    "mature 17+": "Maduro 17+",
    "everyone 10+": "Para todos 10+"  # Agregar más traducciones según sea necesario
}

# Leer los datos del archivo CSV y almacenar las filas
datos = []
with open('Play_Store_Data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # Saltar la primera fila (encabezado)
    for fila in reader:
        datos.append(fila)  # Añadir cada fila al conjunto de datos

# Usar un set para eliminar valores duplicados de los tipos de aplicaciones
tipos = {}  # Diccionario para almacenar la cantidad de aplicaciones por tipo
for fila in datos:
    tipo = fila[6].strip().lower()  # Obtener el tipo de aplicación, limpiando espacios y convirtiendo a minúsculas
    if tipo not in ["nan", "0"]:  # Filtrar los valores no válidos "NaN" y "0"
        tipo_es = tipo_traduccion.get(tipo, tipo.capitalize())  # Traducir el tipo a español y capitalizar
        # Contar las ocurrencias de cada tipo
        if tipo_es in tipos:
            tipos[tipo_es] += 1
        else:
            tipos[tipo_es] = 1

# Ordenar los tipos por la cantidad de aplicaciones
tipos_ord = sorted(tipos.items(), key=lambda x: x[1], reverse=True)
tipos_names = [x[0] for x in tipos_ord]
tipos_values = [x[1] for x in tipos_ord]

# Crear el gráfico de barras para distribución de aplicaciones por tipo
plt.figure(figsize=(10, 6))  # Ajustar el tamaño del gráfico
plt.bar(tipos_names, tipos_values)  # Graficar los tipos y sus cantidades
plt.title('Distribución de Aplicaciones por Tipo')  # Título del gráfico
plt.xlabel('Tipo')  # Etiqueta del eje X
plt.ylabel('Número de Aplicaciones')  # Etiqueta del eje Y
plt.xlim(-0.5, len(tipos_names) - 0.5)  # Ajustar los límites del eje X
plt.tight_layout()  # Ajustar el diseño
plt.show()  # Mostrar el gráfico

# Gráfico 5: Distribución de aplicaciones por género
generos = {}  # Diccionario para almacenar la cantidad de aplicaciones por género
for fila in datos:
    genero = fila[8].strip().lower()  # Obtener el género de la aplicación, limpiando espacios y convirtiendo a minúsculas
    if genero not in ["adults only 18+", "unrated"]:  # Filtrar géneros no deseados
        genero_es = genero_traduccion.get(genero, genero.capitalize())  # Traducir el género y capitalizar
        # Contar las ocurrencias de cada género
        if genero_es in generos:
            generos[genero_es] += 1
        else:
            generos[genero_es] = 1

# Ordenar y graficar el segundo gráfico para distribución de aplicaciones por género
generos_ord = sorted(generos.items(), key=lambda x: x[1], reverse=True)
generos_names = [x[0] for x in generos_ord]
generos_values = [x[1] for x in generos_ord]

# Crear gráfico de barras para distribución de aplicaciones por género
plt.figure(figsize=(10, 6))  # Ajustar el tamaño del gráfico
plt.bar(generos_names, generos_values)  # Graficar los géneros y sus cantidades
plt.title('Distribución de Aplicaciones por Género')  # Título del gráfico
plt.xlabel('Género')  # Etiqueta del eje X
plt.ylabel('Cantidad de Aplicaciones')  # Etiqueta del eje Y
plt.xticks(rotation=90)  # Rotar las etiquetas en el eje X
plt.xlim(-0.5, len(generos_names) - 0.5)  # Ajustar los límites del eje X
plt.tight_layout()  # Ajustar el diseño
plt.show()  # Mostrar el gráfico

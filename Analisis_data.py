# Importación de bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
import csv

# Función para cargar datos del archivo CSV
def cargar_datos():
    # Inicialización de listas para almacenar datos de cada columna
    ratings, reviews, installs, genres, datos = [], [], [], [], []
    # Apertura del archivo CSV
    with open('Play_Store_Data.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Saltar el encabezado
        for row in reader:
            # Filtrar filas que no tengan la cantidad correcta de columnas
            if len(row) == 13:
                try:
                    # Guardar datos de cada columna en listas específicas
                    ratings.append(float(row[2]))
                    reviews.append(float(row[3]))
                    installs.append(int(row[5].replace('+', '').replace(',', '')))
                    genres.append(row[1])
                    datos.append(row)  # Guardar fila completa en 'datos'
                except ValueError:
                    continue  # Ignorar filas con datos no válidos
    # Devolver datos como arrays de NumPy y listas para facilitar el análisis
    return np.array(ratings), np.array(reviews), np.array(installs), genres, datos

# Función para gráfico 1: Distribución de instalaciones
def grafico_instalaciones(installs):
    # Configuración de la figura del gráfico
    plt.figure(figsize=(10, 6))
    # Definición de categorías de instalación
    install_categories = ['0-10K', '10K-100K', '100K-1M', '1M-10M', '10M+']
    # Inicialización de contadores para cada categoría
    install_counts = [0, 0, 0, 0, 0]
    # Clasificación de cada instalación en su categoría correspondiente
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
    # Generación del gráfico de barras
    plt.bar(install_categories, install_counts, color='skyblue')
    plt.xlabel('Categorías de Instalación')
    plt.ylabel('Cantidad de Aplicaciones')
    plt.title('Distribución de Instalaciones de las Aplicaciones')
    plt.tight_layout()
    plt.show()

# Función para gráfico 2: Cantidad de aplicaciones por género
def grafico_genero_cantidad(genres):
    # Identificación de géneros únicos
    unique_genres = set(genres)
    # Conteo de aplicaciones por género
    genre_counts = {genre: genres.count(genre) for genre in unique_genres}
    # Ordenación de géneros por cantidad
    sorted_genre_counts = sorted(genre_counts.items(), key=lambda x: x[1])
    genres_list_sorted, genres_count_sorted = zip(*sorted_genre_counts)
    # Creación del gráfico de barras horizontal
    plt.figure(figsize=(10, 6))
    plt.barh(genres_list_sorted, genres_count_sorted, color='green')
    plt.xlabel('Cantidad de Aplicaciones')
    plt.title('Cantidad de Aplicaciones por Género (Ordenado)')
    plt.tight_layout()
    plt.show()

# Función para gráfico 3: Distribución de Ratings
def grafico_ratings():
    # Inicialización de lista para ratings
    ratings = []
    # Carga de ratings directamente desde el archivo CSV
    with open('Play_Store_Data.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Saltar el encabezado
        for row in reader:
            if len(row) == 13:
                try:
                    rating = float(row[2])
                    ratings.append(rating)
                except ValueError:
                    continue  # Ignorar filas con datos no válidos
    # Definición de intervalos (bins) y etiquetas para el gráfico
    bins = np.arange(1, 6, 1)
    labels = ['[1-2)', '[2-3)', '[3-4)', '[4-5)']
    # Calcular frecuencia de cada rango de rating
    unique_ratings = set(ratings)
    rating_counts, _ = np.histogram(list(unique_ratings), bins=bins)
    # Creación del gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(labels, rating_counts, color='skyblue')
    plt.xlabel('Rango de Ratings')
    plt.ylabel('Cantidad de Aplicaciones')
    plt.title('Distribución de Ratings de Aplicaciones')
    plt.tight_layout()
    plt.show()

# Función para gráfico 4: Distribución de aplicaciones por tipo (Pago o Gratuita)
def grafico_tipo_aplicacion(datos):
    # Traducción de tipo de aplicación para visualización
    tipo_traduccion = {"free": "Gratuita", "paid": "Pago"}
    # Inicialización de diccionario para contar tipos
    tipos = {}
    # Conteo de aplicaciones según tipo
    for fila in datos:
        tipo = fila[6].strip().lower()
        if tipo not in ["nan", "0"]:
            tipo_es = tipo_traduccion.get(tipo, tipo.capitalize())
            tipos[tipo_es] = tipos.get(tipo_es, 0) + 1
    # Ordenar tipos y valores para el gráfico
    tipos_names, tipos_values = zip(*sorted(tipos.items(), key=lambda x: x[1], reverse=True))
    # Creación del gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(tipos_names, tipos_values)
    plt.xlabel('Tipo')
    plt.ylabel('Número de Aplicaciones')
    plt.title('Distribución de Aplicaciones por Tipo')
    plt.tight_layout()
    plt.show()

# Función para gráfico 5: Distribución de aplicaciones por género
def grafico_distribucion_genero(datos):
    # Traducción de categorías de contenido
    genero_traduccion = {"teen": "Adolescente", "everyone": "Para todos", "mature 17+": "Maduro 17+", "everyone 10+": "Para todos 10+"}
    # Inicialización de diccionario para contar categorías de contenido
    generos = {}
    # Conteo de aplicaciones según categoría de contenido
    for fila in datos:
        genero = fila[8].strip().lower()
        if genero not in ["adults only 18+", "unrated"]:
            genero_es = genero_traduccion.get(genero, genero.capitalize())
            generos[genero_es] = generos.get(genero_es, 0) + 1
    # Ordenar categorías de contenido para el gráfico
    generos_names, generos_values = zip(*sorted(generos.items(), key=lambda x: x[1], reverse=True))
    # Creación del gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(generos_names, generos_values)
    plt.xlabel('Género')
    plt.ylabel('Cantidad de Aplicaciones')
    plt.title('Distribución de Aplicaciones por Género')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

# Función principal
def main():
    ratings, reviews, installs, genres, datos = cargar_datos()
    print("Seleccione una opción para ver el gráfico correspondiente:")
    print("a) Distribución de instalaciones")
    print("b) Cantidad de aplicaciones por género")
    print("c) Distribución de Ratings")
    print("d) Distribución de aplicaciones por tipo")
    print("e) Distribución de aplicaciones por género")
    
    opcion = input("Ingrese su opción (a, b, c, d, e): ").strip().lower()
    while opcion not in ["a", "b", "c", "d", "e"]:
        print("Opción no válida. Por favor, seleccione una opción correcta.")
        opcion = input("Ingrese su opción (a, b, c, d, e): ").strip().lower()
    
    
    if opcion == 'a':
        grafico_instalaciones(installs)
    elif opcion == 'b':
        grafico_genero_cantidad(genres)
    elif opcion == 'c':
        grafico_ratings()
    elif opcion == 'd':
        grafico_tipo_aplicacion(datos)
    elif opcion == 'e':
        grafico_distribucion_genero(datos)

if __name__ == "__main__":
    main()

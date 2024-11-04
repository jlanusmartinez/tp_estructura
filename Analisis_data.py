import numpy as np

import matplotlib.pyplot as plt

# Load the CSV file to examine its structure and content
file_path = '/mnt/data/Play Store Data (4).csv'
data = np.genfromtxt(file_path, delimiter=',', dtype=None, encoding='utf-8', names=True)

# Display the first few rows and column names to understand the data
data[:5], data.dtype.names




# Convert necessary columns to arrays
# Filtering non-numeric entries for columns that need to be converted to numeric
ratings = np.array([float(x) if x != 'NaN' else np.nan for x in data['Rating']])
installs = np.array([int(x.replace(',', '').replace('+', '')) if x not in ['Free', 'NaN'] else np.nan for x in data['Installs']])
categories = np.array(data['Category'])

# 1. Gráfico de dispersión: relación entre el número de instalaciones y las calificaciones
plt.figure(figsize=(10, 6))
plt.scatter(installs, ratings, alpha=0.5, c='blue', edgecolor='k')
plt.title("Relación entre número de instalaciones y calificaciones")
plt.xlabel("Número de instalaciones")
plt.ylabel("Calificación")
plt.grid(True)
plt.show()

# 2. Boxplot: distribución de las calificaciones por categoría
# Filtrar las categorías y ratings válidos
valid_ratings = ratings[~np.isnan(ratings)]
valid_categories = categories[~np.isnan(ratings)]

# Agrupar ratings por categorías únicas
unique_categories = np.unique(valid_categories)
ratings_by_category = [valid_ratings[valid_categories == category] for category in unique_categories]

# Gráfico de caja para ver la distribución de ratings en cada categoría
plt.figure(figsize=(12, 8))
plt.boxplot(ratings_by_category, labels=unique_categories, vert=True, patch_artist=True)
plt.xticks(rotation=90)
plt.title("Distribución de calificaciones por categoría")
plt.xlabel("Categoría")
plt.ylabel("Calificación")
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.show()

# Re-load data due to previous code block context reset
data = np.genfromtxt(file_path, delimiter=',', dtype=None, encoding='utf-8', names=True)

# Convert columns to arrays after re-loading data
# Filtering non-numeric entries for columns that need to be converted to numeric
ratings = np.array([float(x) if x != 'NaN' else np.nan for x in data['Rating']])
installs = np.array([int(x.replace(',', '').replace('+', '')) if x not in ['Free', 'NaN'] else np.nan for x in data['Installs']])
categories = np.array(data['Category'])

# 1. Gráfico de dispersión: relación entre el número de instalaciones y las calificaciones
plt.figure(figsize=(10, 6))
plt.scatter(installs, ratings, alpha=0.5, c='blue', edgecolor='k')
plt.title("Relación entre número de instalaciones y calificaciones")
plt.xlabel("Número de instalaciones")
plt.ylabel("Calificación")
plt.grid(True)
plt.show()

# 2. Boxplot: distribución de las calificaciones por categoría
# Filtrar las categorías y ratings válidos
valid_ratings = ratings[~np.isnan(ratings)]
valid_categories = categories[~np.isnan(ratings)]

# Agrupar ratings por categorías únicas
unique_categories = np.unique(valid_categories)
ratings_by_category = [valid_ratings[valid_categories == category] for category in unique_categories]

# Gráfico de caja para ver la distribución de ratings en cada categoría
plt.figure(figsize=(12, 8))
plt.boxplot(ratings_by_category, labels=unique_categories, vert=True, patch_artist=True)
plt.xticks(rotation=90)
plt.title("Distribución de calificaciones por categoría")
plt.xlabel("Categoría")
plt.ylabel("Calificación")
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.show()


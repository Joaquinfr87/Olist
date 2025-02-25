#import os
#os.environ["TCL_LIBRARY"] = r"C:\Users\User\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import numpy as np
from scipy.stats import norm

# Cargar el archivo CSV
df = pd.read_csv('muestra.csv')
#1
# Crear tabla de frecuencias
frecuencia_absoluta = df['Puntuaje'].value_counts().sort_index()
frecuencia_relativa = frecuencia_absoluta / frecuencia_absoluta.sum()

# Crear DataFrame con la tabla de frecuencia
tabla_frecuencia = pd.DataFrame({
    'Puntuaje': frecuencia_absoluta.index,
    'Frecuencia Absoluta': frecuencia_absoluta.values,
    'Frecuencia Relativa': frecuencia_relativa.values
})

# Mostrar tabla de frecuencia
print(tabla_frecuencia)

# Crear el histograma con Seaborn
sns.histplot(df['Puntuaje'], bins=5, kde=False, color='skyblue', edgecolor='black')

# Añadir título y etiquetas
plt.title('Histograma de Puntuaje')
plt.xlabel('Puntuaje')
plt.ylabel('Frecuencia')
plt.xticks([1, 2, 3, 4, 5])

# Mostrar la gráfica
plt.savefig('figure1.png', format='png', dpi=300)
plt.close()  # Cerrar la figura actual
#2

# Crear tabla de frecuencias para Tipo de Pago
frecuencia_absoluta_pago = df['Tipo de Pago'].value_counts().sort_index()
frecuencia_relativa_pago = frecuencia_absoluta_pago / frecuencia_absoluta_pago.sum()

# Crear DataFrame con la tabla de frecuencia
tabla_frecuencia_pago = pd.DataFrame({
    'Tipo de Pago': frecuencia_absoluta_pago.index,
    'Frecuencia Absoluta': frecuencia_absoluta_pago.values,
    'Frecuencia Relativa': frecuencia_relativa_pago.values * 100
})

# Mostrar tabla de frecuencia
print(tabla_frecuencia_pago)

# Crear la gráfica de barras con Seaborn
sns.countplot(x='Tipo de Pago', data=df, palette='viridis', edgecolor='black')

# Calcular los porcentajes
total = len(df)
counts = df['Tipo de Pago'].value_counts(normalize=True) * 100

# Añadir los porcentajes a cada barra
for index, value in enumerate(counts):
    plt.text(index, value + 1, f'{value:.1f}%', ha='center',
             bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3'))

# Definir las nuevas etiquetas
nuevas_etiquetas = ['Tarjeta de Crédito', 'Ticket', 'Voucher', 'Tarjeta débito']

# Cambiar las etiquetas del eje x
plt.xticks(range(len(nuevas_etiquetas)), nuevas_etiquetas, rotation=45)

# Añadir título y etiquetas
plt.title('Distribución de Tipos de Pago')
plt.xlabel('Tipo de Pago')
plt.ylabel('Frecuencia')
plt.tight_layout()

# Mostrar la gráfica
plt.savefig('figure2.png', format='png', dpi=300)
plt.close()  # Cerrar la figura actual
#3
# Suponiendo que tienes una lista de comentarios
comentarios = df['Cuerpo comentario'].tolist()  # Si está en un DataFrame

# Unir todos los comentarios en una sola cadena
texto_comentarios = ' '.join(comentarios)

# Crear la nube de palabras
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(texto_comentarios)

# Mostrar la nube de palabras
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Ocultar los ejes
plt.title('Nube de Palabras de Comentarios')
plt.savefig('figure3.png', format='png', dpi=300)
plt.close()  # Cerrar la figura actual

#4
# Crear tabla de frecuencias para Cuotas de Pago
frecuencia_absoluta_cuotas = df['Cuotas de pago'].value_counts().sort_index()
frecuencia_relativa_cuotas = frecuencia_absoluta_cuotas / frecuencia_absoluta_cuotas.sum()

# Crear DataFrame con la tabla de frecuencia
tabla_frecuencia_cuotas = pd.DataFrame({
    'Cuotas de Pago': frecuencia_absoluta_cuotas.index,
    'Frecuencia Absoluta': frecuencia_absoluta_cuotas.values,
    'Frecuencia Relativa': frecuencia_relativa_cuotas.values * 100
})

# Mostrar tabla de frecuencia
print(tabla_frecuencia_cuotas)

# Crear el histograma con Seaborn
sns.histplot(df['Cuotas de pago'], bins=23, kde=False, color='orange', edgecolor='black')

# Añadir título y etiquetas
plt.title('Histograma de cuotas de pago del 1 al 10')
plt.xlabel('Cuotas de pago')
plt.ylabel('Frecuencia')
plt.xticks([1,2,3,4,5,6,7,8,9,10])
plt.xlim(1,10)

# Mostrar la gráfica
plt.savefig('figure4.png', format='png', dpi=300)
plt.close()  # Cerrar la figura actual
#5
# Crear intervalos para la tabla de distribución
bins = pd.cut(df['Valor del pago'], bins=10)  # Puedes ajustar el número de bins según tus necesidades

# Calcular la tabla de frecuencias agrupadas
tabla_frecuencias = pd.value_counts(bins).reset_index()
tabla_frecuencias.columns = ['Intervalo', 'Frecuencia Absoluta']

# Calcular la frecuencia relativa
tabla_frecuencias['Frecuencia Relativa'] = tabla_frecuencias['Frecuencia Absoluta'] / len(df)

# Ordenar la tabla por intervalo
tabla_frecuencias = tabla_frecuencias.sort_values(by='Intervalo')

# Mostrar la tabla
print("Tabla de Distribución Tipo 2:\n", tabla_frecuencias)

# HISTOGRAMA
plt.figure(figsize=(8, 5))
sns.histplot(df['Valor del pago'], bins=150, kde=True, color='blue')  # Asegúrate de que coincida con el número de bins
plt.xlabel('Valor del Pago')
plt.ylabel('Frecuencia')
plt.title('Histograma de Valor del Pago')
plt.xlim(0,700)
plt.savefig('figure5.png', format='png', dpi=300)
plt.close()  # Cerrar la figura actual

#6

# Configurar Pandas para mostrar todas las filas y columnas
pd.set_option('display.max_rows', None)  # Muestra todas las filas
pd.set_option('display.max_columns', None)  # Muestra todas las columnas

# Calcular la tabla de frecuencias de Categoría Producto
tabla_frecuencias = df['Categoría producto'].value_counts().reset_index()
tabla_frecuencias.columns = ['Categoría Producto', 'Frecuencia Absoluta']
tabla_frecuencias['Frecuencia Relativa'] = tabla_frecuencias['Frecuencia Absoluta'] / len(df)
tabla_frecuencias = tabla_frecuencias.sort_values(by='Categoría Producto')

# Mostrar la tabla completa
print("Tabla de Frecuencias de Categoría Producto:\n", tabla_frecuencias)

# Opcional: Restablecer las opciones de Pandas a su configuración predeterminada
pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')


# Definir el número de gráficas
num_graficas = 4
categorias_por_grafica = len(tabla_frecuencias) // num_graficas + 1  # Asegurarse de que no falten categorías

# Crear gráficas
for i in range(num_graficas):
    plt.figure(figsize=(10, 5))  # Ajustar el tamaño de la figura
    subset = tabla_frecuencias.iloc[i * categorias_por_grafica:(i + 1) * categorias_por_grafica]
    
    ax = sns.barplot(x='Frecuencia Absoluta', y='Categoría Producto', data=subset, palette='magma')
    plt.xlabel('Frecuencia Absoluta')
    plt.ylabel('Categoría Producto')
    plt.title(f'Frecuencia de Categoría Producto - Gráfica {i + 1}')
    
    # Añadir etiquetas de porcentaje
    for p in ax.patches:
        percentage = f'{(p.get_width() / len(df)) * 100:.1f}%'
        ax.annotate(percentage, (p.get_width(), p.get_y() + p.get_height() / 2),
                    ha='left', va='center', color='black')

    # Ajustar el tamaño de las etiquetas en el eje y
    plt.yticks(fontsize=8)  # Cambia el tamaño de la fuente de las etiquetas

    # Guardar la figura
    plt.savefig(f'figure6.{i + 1}.png')  # Guardar como archivo PNG
    plt.close()  # Cerrar la figura
#7
# Crear intervalos para la tabla de distribución
bins = pd.cut(df['Peso producto (g)'], bins=10)  # Puedes ajustar el número de bins según tus necesidades

# Calcular la tabla de frecuencias agrupadas
tabla_frecuencias = pd.value_counts(bins).reset_index()
tabla_frecuencias.columns = ['Intervalo', 'Frecuencia Absoluta']

# Calcular la frecuencia relativa
tabla_frecuencias['Frecuencia Relativa'] = tabla_frecuencias['Frecuencia Absoluta'] / len(df)

# Ordenar la tabla por intervalo
tabla_frecuencias = tabla_frecuencias.sort_values(by='Intervalo')

# Mostrar la tabla
print("Tabla de Distribución Tipo 2:\n", tabla_frecuencias)

# HISTOGRAMA
plt.figure(figsize=(8, 5))
sns.histplot(df['Peso producto (g)'], bins=10, kde=True, color='green')  # Asegúrate de que coincida con el número de bins
plt.xlabel('Peso producto (g)')
plt.ylabel('Frecuencia')
plt.title('Histograma de Peso producto (g)')
#plt.xlim(0,700)
plt.savefig('figure7.png', format='png', dpi=300)
plt.close()  # Cerrar la figura actual


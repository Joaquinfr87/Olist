import os
os.environ["TCL_LIBRARY"] = r"C:\Users\User\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import numpy as np
from scipy.stats import norm

# Cargar el archivo CSV
df = pd.read_csv('muestra.csv')
#1
# Crear el histograma con Seaborn
sns.histplot(df['Puntuaje'], bins=4, kde=False, color='skyblue', edgecolor='black')


# Añadir título y etiquetas
plt.title('Histograma de Puntuaje')
plt.xlabel('Puntuaje')
plt.ylabel('Frecuencia')
plt.xticks([1,2,3,4,5])
# Mostrar la gráfica
plt.show()


#2
# Crear la gráfica de barras con Seaborn
sns.countplot(x='Tipo de Pago', data=df, palette='viridis', edgecolor='black')


# Calcular los porcentajes
total = len(df)
counts = df['Tipo de Pago'].value_counts(normalize=True) * 100

# Añadir los porcentajes a cada barra
for index, value in enumerate(counts):
    plt.text(index, value + 1, f'{value:.1f}%', ha='center'
    ,bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3'))

# Definir las nuevas etiquetas
nuevas_etiquetas = ['Tarjeta de Crédito', 'Ticket', 'Voucher', 'Tarjeta debito']

# Cambiar las etiquetas del eje x
plt.xticks(range(len(nuevas_etiquetas)), nuevas_etiquetas, rotation=45)


# Añadir título y etiquetas
plt.title('Distribución de Tipos de Pago')
plt.xlabel('Tipo de Pago')
plt.ylabel('Frecuencia')
plt.tight_layout()

# Mostrar la gráfica
plt.show()

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
plt.show()

#4
# Crear el histograma con Seaborn
sns.histplot(df['Cuotas de pago'], bins=20, kde=False, color='orange', edgecolor='black')


# Añadir título y etiquetas
plt.title('Histograma de cuotas de pago del 1 al 10')
plt.xlabel('Cuotas de pago')
plt.ylabel('Frecuencia')
plt.xticks([1,2,3,4,5,6,7,8,9,10])
plt.xlim(1,10)
# Mostrar la gráfica
plt.show()

#5
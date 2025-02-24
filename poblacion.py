
import os
os.environ["TCL_LIBRARY"] = r"C:\Users\User\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"

import sqlite3
import matplotlib.pyplot as plt
from collections import Counter
import random

# Conectar a la base de datos
db_connection = sqlite3.connect('sqlite/olist.sqlite')
cursor = db_connection.cursor()

# Ejecutar consulta para obtener las ciudades de los clientes
cursor.execute('SELECT customer_city FROM customers')
registros = cursor.fetchall()

# Ejecutar consulta para contar la cantidad total de clientes
cursor.execute('SELECT COUNT(*) FROM customers')
total_clientes = cursor.fetchone()[0]

# Imprimir el resultado
print(f'\nCantidad total de clientes: {total_clientes}')

# Ejecutar consulta para obtener las ciudades de los vendedores
cursor.execute('SELECT seller_id FROM sellers')
registros = cursor.fetchall()

# Ejecutar consulta para contar la cantidad total de vendedores
cursor.execute('SELECT COUNT(*) FROM sellers')
total_sellers = cursor.fetchone()[0]

# Imprimir el resultado
print(f'Cantidad total de vendedores: {total_sellers}')

import csv
from main import cursor  # Importar cursor desde main.py

# Ejecutar consulta para obtener los puntajes de review
cursor.execute('''
SELECT 
    ov.review_score, op.payment_type, ov.review_comment_title, ov.review_comment_message, 
    op.payment_installments, op.payment_value, pc.product_category_name_english, 
    p.product_weight_g, p.product_length_cm, p.product_width_cm, p.product_height_cm, 
    c.customer_city, o.order_status, oi.freight_value, s.seller_id, 
    op.payment_sequential, o.order_purchase_timestamp, o.order_delivered_carrier_date, 
    o.order_delivered_customer_date, o.order_estimated_delivery_date, 
    ov.review_creation_date, ov.review_answer_timestamp, 
    s.seller_city, s.seller_state, c.customer_state, oi.shipping_limit_date
FROM customers c 
JOIN orders o ON c.customer_id = o.customer_id 
JOIN order_reviews ov ON o.order_id = ov.order_id 
JOIN order_payments op ON op.order_id = o.order_id
JOIN order_items oi ON o.order_id = oi.order_id 
JOIN products p ON p.product_id = oi.product_id
JOIN product_category_name_translation pc ON pc.product_category_name = p.product_category_name
JOIN sellers s ON oi.seller_id = s.seller_id
WHERE ov.review_comment_message IS NOT NULL 
AND ov.review_comment_message <> ''
ORDER BY RANDOM() 
LIMIT 4054;
''')

# Obtener los resultados
registros = cursor.fetchall()

# Guardar los resultados en un archivo CSV
with open("reviews.csv", mode="w", newline="", encoding="utf-8") as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    
    # Escribir la cabecera
    escritor_csv.writerow([
        "Puntuaje", "Tipo de Pago", "Título comentario", "Cuerpo comentario",
        "Cuotas de pago", "Valor del pago", "Categoría producto",
        "Peso producto (g)", "Largo producto (cm)", "Ancho producto (cm)", "Alto producto (cm)",
        "Ciudad cliente", "Estado orden", "Precio envío", "ID vendedor",
        "Secuencia de pago", "Tiempo compra pedido", "Fecha de cargo",
        "Fecha de entrega prevista", "Fecha estimada de entrega",
        "Creación comentario", "Lapso tiempo respuesta", 
        "Ciudad vendedor", "Estado vendedor", "Estado cliente",
        "Fecha límite de envío"
    ])

    # Escribir los registros
    escritor_csv.writerows(registros)

print("Los datos se han guardado en 'reviews.csv'")
import pika
import json

# --- CONFIGURA ESTO ---
RUTA_IMAGEN_LOCAL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ31lIAI4yE088JnG3PqEyTqyp0xrbNsaoH1w&s" 

def simular_companero():
    payload = {
        "student_id": "ALUMNO_001",
        "session_id": "examen_titulacion_2026",
        "chunk_index": 1,
        "image_url": RUTA_IMAGEN_LOCAL
    }

    try:
        # Nos conectamos a RabbitMQ
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        # Aseguramos que la cola exista
        QUEUE_NAME = 'q_snapshots'
        channel.queue_declare(queue=QUEUE_NAME, durable=True)

        # Metemos el mensaje a la cola
        channel.basic_publish(
            exchange='',
            routing_key=QUEUE_NAME,
            body=json.dumps(payload),
            properties=pika.BasicProperties(
                delivery_mode=2,  # Hace que el mensaje sea persistente (no se borra si RabbitMQ se reinicia)
            )
        )
        print(f"✅ [Productor] Se encoló la URL de la imagen exitosamente en '{QUEUE_NAME}'.")
        connection.close()
        
    except Exception as e:
        print(f"❌ Error conectando a RabbitMQ: {e}")

if __name__ == "__main__":
    simular_companero()
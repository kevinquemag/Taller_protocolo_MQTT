import json
import paho.mqtt.client
from datetime import datetime

# Callback cuando el cliente se conecta al broker
def on_connect(client, userdata, flags, rc):
    print('Conectado al broker con código de resultado (%s)' % rc)
    # Suscribirse al tópico del sensor de luz
    client.subscribe(topic='casa/habitacion/sensor_luz', qos=2)

# Callback cuando se recibe un mensaje del tópico suscrito
def on_message(client, userdata, message):
    print('------------------------------')
    print('Tópico: %s' % message.topic)
    payload = message.payload.decode('utf-8')
    print('Payload recibido: %s' % payload)

    try:
        # Convertir el payload ingresado (solo value) a un valor entero
        value = int(payload)

        # Crear el resto del JSON con valores predeterminados
        data = {
            "device_id": "5ee9df89-a719-4e9a-ac54-84b9c3096f40",
            "event_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
            "value": value,
            "accuracy": 0.98  # Supongamos que la precisión es siempre alta
        }

        print('Datos procesados: %s' % json.dumps(data, indent=4))

        # Control de luces basado en los datos del sensor
        if data["value"] < 50 and data["accuracy"] > 0.9:
            print('El sensor indica poca luz. Las luces serán encendidas.')
        else:
            print('El sensor indica luz suficiente. Las luces serán apagadas.')
    except ValueError:
        print('Error: El mensaje recibido no es un valor numérico válido.')

# Función principal para configurar y ejecutar el cliente MQTT
def main():
    # Crear un cliente MQTT
    client = paho.mqtt.client.Client(client_id='controlador_luces', clean_session=False)
    client.on_connect = on_connect
    client.on_message = on_message

    # Conectar al broker MQTT
    client.connect(host='127.0.0.1', port=1883)

    # Mantener el cliente en funcionamiento
    client.loop_forever()

if __name__ == '__main__':
    main()



# 3.	Explique qué cambios debería de hacer en su código para soportar 2 sensores de luz adicionales y 
# 2 motores de cortinas enrollables.  

# import json
# import paho.mqtt.client
# from datetime import datetime

# # Lista de tópicos
# TOPICOS_SENSORES = [
#     'casa/habitacion/sensor_luz1',
#     'casa/habitacion/sensor_luz2',
#     'casa/habitacion/sensor_luz3'
# ]

# TOPICOS_MOTORES = [
#     'casa/habitacion/motor_cortina1',
#     'casa/habitacion/motor_cortina2'
# ]

# # Callback cuando el cliente se conecta al broker
# def on_connect(client, userdata, flags, rc):
#     print('Conectado al broker con código de resultado (%s)' % rc)
#     # Suscribirse a todos los tópicos
#     for topico in TOPICOS_SENSORES + TOPICOS_MOTORES:
#         client.subscribe(topico, qos=2)
#         print(f"Suscrito a {topico}")

# # Callback cuando se recibe un mensaje del tópico suscrito
# def on_message(client, userdata, message):
#     print('------------------------------')
#     print(f"Tópico: {message.topic}")
#     payload = message.payload.decode('utf-8')
#     print(f"Payload recibido: {payload}")

#     try:
#         # Procesar mensajes de sensores de luz
#         if message.topic in TOPICOS_SENSORES:
#             value = int(payload)
#             data = {
#                 "device_id": f"{message.topic.split('/')[-1]}",
#                 "event_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
#                 "value": value,
#                 "accuracy": 0.98
#             }
#             print('Datos procesados: %s' % json.dumps(data, indent=4))

#             # Lógica para control de luces
#             if data["value"] < 50 and data["accuracy"] > 0.9:
#                 print(f'[Sensor {data["device_id"]}] Poca luz detectada. Las luces serán encendidas.')
#             else:
#                 print(f'[Sensor {data["device_id"]}] Luz suficiente detectada. Las luces serán apagadas.')

#         # Procesar mensajes de motores de cortinas
#         elif message.topic in TOPICOS_MOTORES:
#             comando = payload.lower()
#             if comando == "subir":
#                 print(f'[Motor {message.topic.split("/")[-1]}] Cortinas subiendo...')
#             elif comando == "bajar":
#                 print(f'[Motor {message.topic.split("/")[-1]}] Cortinas bajando...')
#             else:
#                 print(f'[Motor {message.topic.split("/")[-1]}] Comando desconocido: {comando}')

#     except ValueError:
#         print('Error: El mensaje recibido no es un valor numérico válido.')

# # Función principal para configurar y ejecutar el cliente MQTT
# def main():
#     client = paho.mqtt.client.Client(client_id='controlador_dispositivos', clean_session=False)
#     client.on_connect = on_connect
#     client.on_message = on_message

#     # Conectar al broker MQTT
#     client.connect(host='127.0.0.1', port=1883)

#     # Mantener el cliente en funcionamiento
#     client.loop_forever()

# if __name__ == '__main__':
#     main()

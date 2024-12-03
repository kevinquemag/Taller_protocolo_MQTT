/*--Crear el archivo con la configuración del servidor--*/

El archivo lo he creado mediante visual estudio code en la carpeta MQTT que indica en el video. Su contenido es el mismo:
listener 1883 127.0.0.1
allow_anonymous true

/*----Instalar Mosquitto----*/

sudo aptitude install mosquitto

sudo aptitude install mosquitto-clients

/*---En este caso mi archivo .conf lo llame mosquito con una sola "T"---*/

mosquitto -c mosquito.conf

/*--Configurar un subscriptor (practica inicial)--*/

mosquitto_sub -h 127.0.0.1 -p 1883 -t "casa/cocina/nevera" -v

/*--Publicar mensajes en un topic (practica inicial)--*/

mosquitto_pub -h 127.0.0.1 -p 1883 -t "casa/cocina/nevera" -m "{ temp: 30 }"

######################### Tarea con las instrucciones para la ejecución y verificación del código

/*-- Para el subscriptor basado en el video de muestra* --/

mosquitto_sub -h 127.0.0.1 -p 1883 -t "casa/habitacion/sensor_luz" -v

/*-- Conserve el archivo subs.py y modifique el código --*/

gedit subs.py

/*-- Instale la librería paho-mqtt --*/

pip install --user paho-mqtt

/*-- Al momento de querer correr el archivo subs.py tenia un error pues mi sistema tenia un entorno de Python gestionado para protección de paquetes por lo que use un entorno virtual que fue lo que me resulto mas sencillo--*/

python3 -m venv myenv

/*-- Activar el entorno virtual--*/

source myenv/bin/activate

/*-- Dentro del entorno virtual instale la librería paho-mqtt --*/

pip install paho-mqtt

/*-- volviéndolo a ejecutar su funcionamiento fue el esperado --*/

python3 subs.py

############### Evaluación del código usando al publicador y conexión

comando: mosquitto_pub -h 127.0.0.1 -p 1883 -t "casa/habitacion/sensor_luz" -m "30"

respuesta:

Payload recibido: 30

Datos procesados: {
    
    "device_id": "5ee9df89-a719-4e9a-ac54-84b9c3096f40",
    "event_time": "2024-12-03 04:24:28.943025",
    "value": 30,
    "accuracy": 0.98
}
El sensor indica poca luz. Las luces serán encendidas.

Comando: mosquitto_pub -h 127.0.0.1 -p 1883 -t "casa/habitacion/sensor_luz" -m "70"

respuesta:

Tópico: casa/habitacion/sensor_luz

Payload recibido: 70
Datos procesados: {
    
    "device_id": "5ee9df89-a719-4e9a-ac54-84b9c3096f40",
    "event_time": "2024-12-03 09:10:49.962979",
    "value": 70,
    "accuracy": 0.98
}
El sensor indica luz suficiente. Las luces serán apagadas.

Comando: mosquitto_pub -h 127.0.0.1 -p 1883 -t "casa/habitacion/sensor_luz" -m "50"

respuesta: 

Tópico: casa/habitacion/sensor_luz

Payload recibido: 50
Datos procesados: {

    "device_id": "5ee9df89-a719-4e9a-ac54-84b9c3096f40",
    "event_time": "2024-12-03 09:11:44.079507",
    "value": 50,
    "accuracy": 0.98
}
El sensor indica luz suficiente. Las luces serán apagadas.

![image](https://github.com/user-attachments/assets/6993ede1-f36c-4e5a-b548-9e8ed90c092f)


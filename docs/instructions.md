# Instrucciones para el Sistema de Detección Facial con Alarma 🚨

## Introducción

Este documento proporciona instrucciones sobre cómo instalar y utilizar el sistema de detección facial con alarma. Este sistema utiliza OpenCV y MediaPipe para detectar caras en tiempo real y activar una alarma visual y sonora cuando se detecta un número específico de caras.

## Instalación 🛠️

1. **Clonar el repositorio:**
   Abre una terminal y ejecuta el siguiente comando para clonar el repositorio:
   ```bash
   git clone https://github.com/jrodriguezblangino/FaceDetectorAlarm
   cd tu_repositorio
   ```

2. **Instalar las dependencias:**
   Asegúrate de tener Python y pip instalados. Luego, instala las dependencias necesarias ejecutando:
   ```bash
   pip install -r requirements.txt
   ```

## Uso 🚀

1. **Ejecutar el programa:**
   Para iniciar el sistema, ejecuta el siguiente comando en la terminal:
   ```bash
   python src/main.py
   ```

2. **Configurar el umbral de activación:**
   Se te pedirá que ingreses el umbral de personas que deseas detectar para activar la alarma. Introduce un número entero y presiona Enter.

3. **Interacción con el sistema:**
   - Cuando se detecten caras y el número supere el umbral, se activará la alarma.
   - Se te preguntará si deseas reiniciar el chequeo de caras. Si eliges "s", podrás ingresar un nuevo umbral.

## Características 🌟

- **Detección de caras en tiempo real:** Utiliza la cámara para detectar caras en vivo.
- **Alarma visual y sonora:** Se activa cuando se supera el umbral de detección.
- **Interfaz de línea de comandos:** Permite configurar el umbral de activación y la duración de la alarma.

## Contribuciones 🤝

Las contribuciones son bienvenidas. Si deseas contribuir al proyecto, por favor abre un issue o un pull request en GitHub.

---

¡Gracias por usar el Sistema de Detección Facial con Alarma! 🎉


---



---Instructions for Facial Detection System with Alarm 🚨
======================================================

Introduction
------------

This document provides instructions on how to install and use the facial detection system with alarm. This system uses OpenCV and MediaPipe to detect faces in real-time and activate a visual and sound alarm when a specific number of faces is detected.

Installation 🛠️
----------------

1.  bashgit clone https://github.com/jrodriguezblangino/FaceDetectorAlarm.gitcd your\_repository
    
2.  bashpip install -r requirements.txt
    

Usage 🚀
--------

1.  bashpython src/main.py
    
2.  **Configure the activation threshold:**

You will be asked to enter the threshold of people you want to detect to activate the alarm. Enter an integer and press Enter.
    
3.  **Interaction with the system:**
    
    *   When faces are detected and the number exceeds the threshold, the alarm will activate.
        
    *   You will be asked if you want to restart the face check. If you choose "y", you can enter a new threshold.
        

Features 🌟
-----------

*   **Real-time face detection:** Uses the camera to detect faces live.
    
*   **Visual and sound alarm:** Activates when the detection threshold is exceeded.
    
*   **Command line interface:** Allows you to configure the activation threshold and alarm duration.
    

Contributions 🤝
----------------

Contributions are welcome. If you wish to contribute to the project, please open an issue or a pull request on GitHub.

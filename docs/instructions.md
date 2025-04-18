# Instrucciones para el Sistema de Detección Facial con Alarma 🚨

## Introducción

Este documento proporciona instrucciones sobre cómo instalar y utilizar el sistema de detección facial con alarma. Este sistema utiliza OpenCV y MediaPipe para detectar caras en tiempo real y activar una alarma visual y sonora cuando se detecta un número específico de caras.

## Instalación 🛠️

1. **Clonar el repositorio:**
   Abre una terminal y ejecuta el siguiente comando para clonar el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
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

## Contacto 📧

Si tienes preguntas o necesitas ayuda, no dudes en contactarme a través de mi perfil de GitHub.

---

¡Gracias por usar el Sistema de Detección Facial con Alarma! 🎉

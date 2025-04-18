import cv2
import argparse
from config import settings
from detector.face_detector import FaceDetector
from alarm.alarm_system import AlarmSystem
import time

def setup_cli() -> argparse.Namespace:
    """Configura los argumentos de línea de comandos.
    
    Returns:
        argparse.Namespace: Los argumentos de línea de comandos.
    """
    parser = argparse.ArgumentParser(description="Sistema de detección facial con alarma")
    parser.add_argument("-t", "--threshold", type=int, default=5,
                        help="Umbral de personas para activar alarma")
    parser.add_argument("-d", "--duration", type=int, default=5,
                        help="Duración de la alarma en segundos")
    return parser.parse_args()

def main():
    """Función principal que ejecuta el sistema de detección facial con alarma."""
    args = setup_cli()
    
    # Preguntar al usuario cuántas personas se desean detectar para disparar la alarma
    new_threshold = int(input("Ingrese el umbral de personas para activar la alarma: "))
    
    # Inicializar el detector de caras
    detector = FaceDetector(
        min_detection_confidence=settings.MIN_FACE_CONFIDENCE,
        max_num_faces=settings.MAX_FACES
    )
    
    # Inicializar el sistema de alarma
    alarm_system = AlarmSystem(
        trigger_count=new_threshold,  # Usar el nuevo umbral ingresado
        duration=args.duration
    )
    
    # Captura de video desde la cámara
    cap = cv2.VideoCapture(0)
    
    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            # Redimensionar frame para visualización
            frame = cv2.resize(frame, (settings.DISPLAY_WIDTH, settings.DISPLAY_HEIGHT))
            
            # Detectar caras
            faces = detector.detect_faces(frame)
            
            # Dibujar cuadros y contador
            for (x, y, w, h) in faces:
                color = settings.ALARM_COLOR if alarm_system.alarm_active else settings.TEXT_COLOR
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            
            # Mostrar contador
            text = f"Personas: {len(faces)}/{new_threshold}"
            color = settings.ALARM_COLOR if alarm_system.alarm_active else settings.TEXT_COLOR

            # Fondo para mejor legibilidad 
            (text_width, text_height), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, settings.FONT_SCALE, 2)
            cv2.rectangle(frame, (10, 10), (20 + text_width, 40 + text_height), (0, 0, 0), -1)

            # Texto principal
            cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, settings.FONT_SCALE, (0, 0, 255), 2)
            
            # Verificar alarma
            alarm_system.check_alarm(len(faces))
            alarm_system.update()
            
            if alarm_system.alarm_active:
                cap.release()  # Cerrar la cámara
                cv2.destroyAllWindows()  # Cerrar la ventana de OpenCV
                cv2.imshow("Face Scanner Alarm", frame)
                time.sleep(alarm_system.duration)  # Esperar la duración de la alarma
                alarm_system.update()  # Actualizar el estado de la alarma
                restart = input("¿Desea reiniciar el chequeo de caras? (s/n): ")
                if restart.lower() == 's':
                    new_threshold = int(input("Ingrese el nuevo umbral de personas para activar la alarma: "))
                    alarm_system.trigger_count = new_threshold
                    cap = cv2.VideoCapture(0)  # Reabrir la cámara
                else:
                    break
            else:
                cv2.imshow("Face Scanner Alarm", frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
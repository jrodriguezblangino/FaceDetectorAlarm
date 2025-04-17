import cv2
import argparse
from typing import Tuple
from config import settings
from detector.face_detector import FaceDetector
from alarm.alarm_system import AlarmSystem

def setup_cli() -> argparse.Namespace:
    """Configura los argumentos de línea de comandos."""
    parser = argparse.ArgumentParser(description="Sistema de detección facial con alarma")
    parser.add_argument("-t", "--threshold", type=int, default=5,
                       help="Umbral de personas para activar alarma")
    parser.add_argument("-d", "--duration", type=int, default=5,
                       help="Duración de la alarma en segundos")
    return parser.parse_args()

def main():
    args = setup_cli()
    
    detector = FaceDetector(
        min_detection_confidence=settings.MIN_FACE_CONFIDENCE,
        max_num_faces=settings.MAX_FACES
    )
    
    alarm_system = AlarmSystem(
        trigger_count=args.threshold,
        duration=args.duration
    )
    
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
            text = f"Personas: {len(faces)}/{args.threshold}"
            cv2.putText(frame, text, (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, settings.FONT_SCALE,
                       settings.ALARM_COLOR if alarm_system.alarm_active else settings.TEXT_COLOR, 2)
            
            # Verificar alarma
            alarm_system.check_alarm(len(faces))
            alarm_system.update()
            
            cv2.imshow("Face Scanner Alarm", frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q') or alarm_system.alarm_active:
                break
                
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
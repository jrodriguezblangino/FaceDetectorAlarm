import cv2
import argparse
from typing import Tuple
from config import settings
from detector.face_detector import FaceDetector
from alarm.alarm_system import AlarmSystem

def main():
    """Función principal del 2programa."""
    try:
        threshold = int(input("Ingrese el umbral de personas para activar la alarma: "))
        duration = int(input("Ingrese la duración de la alarma en segundos: "))

        detector = FaceDetector(
            min_detection_confidence=settings.MIN_FACE_CONFIDENCE,
            max_num_faces=settings.MAX_FACES
        )

        alarm_system = AlarmSystem(
            trigger_count=threshold,
            duration=duration
        )

        cap = cv2.VideoCapture(0)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            frame = cv2.resize(frame, (settings.DISPLAY_WIDTH, settings.DISPLAY_HEIGHT))
            
            faces = detector.detect_faces(frame)
            
            for (x, y, w, h) in faces:
                color = settings.ALARM_COLOR if alarm_system.alarm_active else settings.TEXT_COLOR
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            
            text = f"Personas: {len(faces)}/{threshold}"
            cv2.putText(frame, text, (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, settings.FONT_SCALE,
                       settings.ALARM_COLOR if alarm_system.alarm_active else settings.TEXT_COLOR, 2)
            
            alarm_system.check_alarm(len(faces))
            alarm_system.update()
            
            cv2.imshow("Face Scanner Alarm", frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q') or alarm_system.alarm_active:
                break
                
    except ValueError:
        print("Por favor, ingrese valores numéricos para el umbral y la duración.")
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
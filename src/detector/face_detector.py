import cv2
import mediapipe as mp
from typing import Tuple, List, Optional
import numpy as np

class FaceDetector:
    """Clase para detección facial en tiempo real usando MediaPipe.
    
    Attributes:
        min_detection_confidence (float): Confianza mínima para detección
        max_num_faces (int): Número máximo de caras a detectar
    """
    
    def __init__(self, min_detection_confidence: float = 0.7, max_num_faces: int = 5):
        self.min_detection_confidence = min_detection_confidence
        self.max_num_faces = max_num_faces
        self._init_mediapipe()

    def _init_mediapipe(self) -> None:
        """Inicializa los modelos de MediaPipe."""
        self.face_mesh = mp.solutions.face_mesh.FaceMesh(
            max_num_faces=self.max_num_faces,
            refine_landmarks=True,
            min_detection_confidence=self.min_detection_confidence
        )

    def detect_faces(self, frame: np.ndarray) -> List[Tuple[int, int, int, int]]:
        """Detecta caras en un frame de video.
        
        Args:
            frame: Frame de video en formato BGR
            
        Returns:
            Lista de rectángulos (x, y, ancho, alto) de caras detectadas
        """
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb_frame)
        
        faces = []
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                landmarks = np.array([(lm.x, lm.y) for lm in face_landmarks.landmark])
                x_min, y_min = landmarks.min(axis=0)
                x_max, y_max = landmarks.max(axis=0)
                
                height, width = frame.shape[:2]
                x_min = int(x_min * width)
                x_max = int(x_max * width)
                y_min = int(y_min * height)
                y_max = int(y_max * height)
                
                faces.append((x_min, y_min, x_max - x_min, y_max - y_min))
        
        return faces
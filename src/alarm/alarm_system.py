import time
import winsound
from typing import Callable

class AlarmSystem:
    """Maneja las alarmas visuales y sonoras.
    
    Attributes:
        trigger_count (int): Número de caras que activan la alarma
        duration (int): Duración de la alarma en segundos
    """
    
    def __init__(self, trigger_count: int = 5, duration: int = 5):
        self.trigger_count = trigger_count
        self.duration = duration
        self.alarm_active = False
        self.start_time = 0.0

    def check_alarm(self, face_count: int) -> bool:
        """Verifica si se debe activar la alarma.
        
        Args:
            face_count: Número actual de caras detectadas
            
        Returns:
            True si la alarma debe activarse
        """
        if face_count >= self.trigger_count and not self.alarm_active:
            self.activate_alarm()
            return True
        return False

    def activate_alarm(self) -> None:
        """Activa la alarma visual y sonora."""
        self.alarm_active = True
        self.start_time = time.time()
        winsound.Beep(1000, 1000)  # Frecuencia 1000Hz por 1 segundo

    def update(self) -> None:
        """Actualiza el estado de la alarma."""
        if self.alarm_active and (time.time() - self.start_time) > self.duration:
            self.alarm_active = False
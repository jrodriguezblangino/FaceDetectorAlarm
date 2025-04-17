import os
from typing import Final

# Configuración de detección
MIN_FACE_CONFIDENCE: Final[float] = float(os.getenv("MIN_FACE_CONFIDENCE", "0.7"))
MAX_FACES: Final[int] = int(os.getenv("MAX_FACES", "5"))
ALARM_DURATION: Final[int] = int(os.getenv("ALARM_DURATION", "5"))  # en segundos

# Configuración de visualización
DISPLAY_WIDTH: Final[int] = 800
DISPLAY_HEIGHT: Final[int] = 600
FONT_SCALE: Final[float] = 1.2
TEXT_COLOR: Final[tuple[int, int, int]] = (0, 255, 0)  # BGR
ALARM_COLOR: Final[tuple[int, int, int]] = (0, 0, 255)
# Face Detection Alarm System 🚨

This project is a face detection system that activates a visual and sound alarm when a specific number of faces are detected. It uses OpenCV and MediaPipe libraries for real-time face detection.

This project emerges as a practical application of the OpenCV library and its complementary tools for real-time facial detection. The developed system allows monitoring the presence of people in a specific space, triggering configurable alerts based on predefined thresholds.

Use Cases
---------

The system offers multiple practical applications:

*   **Event management**: Automatically detect when the necessary quorum has been reached to begin a conference or meeting.
    
*   **Public transportation**: Determine when a vehicle has reached its optimal passenger capacity.
    
*   **Capacity control**: Monitor in real-time the occupancy of public or private spaces.
    
*   **Preventive security**: Generate alerts when the density of people in a restricted area exceeds established limits.
    
*   **Pedestrian traffic analysis**: Collect data on people flows to optimize spaces.
    

This tool demonstrates how computer vision can provide automated solutions for counting and monitoring people, eliminating the need for constant manual supervision.

## Features 🌟
- Real-time face detection.
- Visual and sound alarm that activates when a detection threshold is exceeded.
- Command-line interface to configure the activation threshold and alarm duration.

## Installation 🛠️

1. Clone the repository:
   ```bash
   git clone https://github.com/jrodriguezblangino/FaceDetectorAlarm
   cd your_repository
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage 🚀

Run the program with the following command:
```bash
python src/main.py
```

You will be prompted to enter the number of people to trigger the alarm.

## Contributions 🤝

Contributions are welcome. If you would like to contribute, please open an issue or a pull request.

## Spanish Version 🇪🇸

Para la versión en español de este README, [haz clic aquí](README.md).

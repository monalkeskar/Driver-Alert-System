# Real-Time Driver Monitoring and Alert System

## Overview

The Real-Time Driver Monitoring and Alert System is an AI-powered computer vision application designed to improve road safety by detecting distracted driving behaviors. Using a webcam, the system monitors the driver's activities in real time and generates alerts when unsafe behavior is detected.

The project integrates object detection and facial landmark analysis to identify mobile phone usage and monitor driver focus, providing immediate audio and visual feedback.

---

## Features

- Real-time mobile phone detection using YOLOv8
- Driver focus monitoring using MediaPipe Face Mesh
- Audio and visual alert generation
- Real-time webcam monitoring
- Lightweight and efficient implementation
- Rule-based decision engine for alert prioritization

---

## Technologies Used

- Python
- OpenCV
- YOLOv8 (Ultralytics)
- MediaPipe
- NumPy

---

## Project Structure

```
Driver-Alert-System/
│
├── main.py
├── detection.py
├── decision.py
├── focus.py
├── alert.py
├── yolov8n.pt
├── beep.wav
├── README.md
├── requirements.txt
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/monalkeskar/Driver-Alert-System.git
```

### Navigate to the project directory

```bash
cd Driver-Alert-System
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python main.py
```

---

## How It Works

1. Captures live video from the webcam.
2. Detects the driver and mobile phone using YOLOv8.
3. Monitors head orientation using MediaPipe Face Mesh.
4. Processes detection results through a decision engine.
5. Generates audio and visual alerts when unsafe behavior is detected.

---

## Future Enhancements

- Driver drowsiness detection
- Seatbelt detection
- Custom-trained YOLO model
- GPS-based emergency notifications
- Deployment on embedded devices such as Raspberry Pi

---

## Team Members

- Monal A Keskar
- Sweezal Rodrigues
- Tejas R
- K. P. Tejas Srinivas

---

## License

This project was developed as part of an academic mini project and is intended for educational purposes.

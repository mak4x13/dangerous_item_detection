# Smart Security System – Dangerous Item Detection

This repository contains a YOLOv8-based object detection model trained to detect dangerous items for smart security applications.

## Detected Classes
The model detects the following classes in this exact order:

0. Machete  
1. Knife  
2. Baseball Bat  
3. Rifle  
4. Gun  

## Model Details
- Architecture: YOLOv8n
- Input size: 640x640
- Framework: Ultralytics YOLO
- Training epochs: 55
- Device used: NVIDIA Tesla T4 (Colab)

## Performance (Test Set)
- Precision: 0.888
- Recall: 0.806
- mAP@50: 0.882
- mAP@50–95: 0.633

## Installation

```bash
pip install -r requirements.txt
```

Real-Time Detection (Webcam)
```bash
python realtime_detection.py
```
Press q to exit the webcam window.

Recommended confidence threshold: 0.25

Training Your Own Model
Place your dataset in the following structure:

```bash
Dangerous_Items/
├── images/
│   ├── train
│   ├── val
│   └── test
├── labels/
│   ├── train
│   ├── val
│   └── test
```
Then run:

```bash
python train.py
```

Or for detailed code execution check: Dangerous_Item_Detection_Model_Training.ipynb


Notes\
The dataset is not included in this repository.\
Lower confidence thresholds improve recall for security-critical use cases.

License\
This project uses Ultralytics YOLO under the AGPL-3.0 license.

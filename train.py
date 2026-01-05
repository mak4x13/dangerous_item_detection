from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="configs/Dangerous_Items.yaml",
    epochs=55,
    imgsz=640,
    batch=16
)

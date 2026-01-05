import cv2
from ultralytics import YOLO

# Load trained model
model = YOLO("best.pt")

model.model.names = {
    0: "machete",
    1: "knife",
    2: "baseball_bat",
    3: "rifle",   
    4: "gun"
}

# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

# Optional tuning
CONF_THRESHOLD = 0.30

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run inference
    results = model.predict(
        source=frame,
        imgsz=640,
        conf=CONF_THRESHOLD,
        stream=False
    )

    # Draw detections
    annotated_frame = results[0].plot()

    cv2.imshow("Smart Security - Dangerous Item Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

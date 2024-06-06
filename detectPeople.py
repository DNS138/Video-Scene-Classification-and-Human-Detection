import cv2

# Load pre-trained Caffe model for human detection
net = cv2.dnn.readNetFromCaffe("./deploy.prototxt", "./res10_300x300_ssd_iter_140000.caffemodel")

def detect_people(frame):
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            return True
    return False

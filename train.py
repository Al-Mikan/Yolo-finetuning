from ultralytics import YOLO

# Load a model
model = YOLO('yolov8s.pt')  # load a partially trained model

# Resume training
results = model.train(data='datasets/data.yaml', epochs=30)
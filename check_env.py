import cv2, torch, ultralytics
print("OpenCV :", cv2.__version__)
print("PyTorch:", torch.__version__, "GPU =", torch.cuda.is_available())
print("YOLOv8 :", ultralytics.__version__)


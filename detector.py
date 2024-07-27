from ultralytics import YOLO

modelo = YOLO('yolov8n.pt')
modelo.predict(source='0',show=True)

#PS C:\Users\chris> cd detector
#PS C:\Users\chris\detector> python -m venv venv
#PS C:\Users\chris\detector> venv\Scripts\activate
#(venv) PS C:\Users\chris\detector> pip install ultralytics
#PS C:\Users\chris\detector> python detector.py

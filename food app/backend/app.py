from flask_cors import CORS
from flask import Flask, request, jsonify
import os 
from PIL import Image
from ultralytics import YOLO
import pandas as pd

app = Flask(__name__) 
CORS(app)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    
    image_file = request.files['image']
    image_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
    image_file.save(image_path)
    # Predict using YOLOv8
    results = model(image_path)
    names = results[0].names
    detections = results[0].boxes.cls.tolist()

# Load model and calorie data
model = YOLO('yolov8n.pt')  # You can change this to a food-specific model
calories = {
    'pizza': 266,
    'burger': 295,
    'banana': 105,
    'apple': 95,
    'cake': 350,
    'fries': 365
}


    
    if not detections:
        return jsonify({'result': 'No food detected'}), 200

    food_items = [names[int(cls)] for cls in detections]
    calorie_info = [
        {'item': food, 'calories': calories.get(food.lower(), 'Unknown')}
        for food in food_items
    ]

    return jsonify({
        'detected': calorie_info
    })

if __name__ == '__main__':
    app.run(debug=True)

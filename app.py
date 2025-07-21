import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("leaf_disease_model.h5")

# Class labels
class_names = ["Pepper Bell - Bacterial Spot", "Pepper Bell - Healthy"]

st.set_page_config(page_title="Leaf Disease Detector", layout="centered")
st.title("🌿 Leaf Disease Detection")
st.write("Upload a leaf image to detect if it's healthy or diseased.")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image", use_column_width=True)

    img = img.resize((224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    class_index = np.argmax(prediction)
    confidence = np.max(prediction)

    st.subheader("Prediction:")
    st.success(f"🩺 {class_names[class_index]} ({confidence*100:.2f}%)")

    if class_index == 0:
        st.warning("⚠️ Recommended Treatment:")
        st.markdown("""
        - Remove infected leaves  
        - Apply copper-based fungicides  
        - Avoid overhead watering  
        - Use disease-resistant varieties
        """)

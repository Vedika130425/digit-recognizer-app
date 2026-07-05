import streamlit as st
from PIL import Image, ImageOps
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('digit_recognizer.h5')

st.title("✍️ Handwritten Digit Recognizer")
st.write("Upload an image of a single handwritten digit (0–9)")

uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert('L')

    img_array_check = np.array(img)
    if img_array_check.mean() > 127:
        img = ImageOps.invert(img)

    img = img.resize((28, 28))
    st.image(img, caption="Processed Image (28x28)", width=150)

    img_array = np.array(img).reshape(1, 28, 28, 1) / 255.0

    if st.button("Predict"):
        pred = model.predict(img_array)
        digit = np.argmax(pred)
        confidence = np.max(pred) * 100
        st.subheader(f"Prediction: {digit}")
        st.write(f"Confidence: {confidence:.2f}%")

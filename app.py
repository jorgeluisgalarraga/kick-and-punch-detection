import streamlit as st
from PIL import Image

from ultralytics import YOLO

# Load the Yolo Model
model = YOLO('./runs/classify/train7/weights/best.pt')  # load a custom model

def predict(image):
    image = Image.open(image)
    results = model(image)
    probs = results[0].probs.data.tolist()
    names = results[0].names

    # Create a dictionary mapping class labels to probabilities
    prob_dict = {names[i]: prob for i, prob in enumerate(probs)}

    # Find the class with the highest probability
    max_class = max(prob_dict, key=prob_dict.get)
    max_prob = prob_dict[max_class]

    # st.subheader('Predicted class:')
    # st.write(f'**{(max_class).capitalize()}** with a probability of {max_prob: .3f}')
    return max_class, max_prob



st.title("Kick and Punch Classifier with YoloV8")

col1, col2 = st.columns(2)

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])


if uploaded_file is not None:
    image = Image.open(uploaded_file)
    max_class, max_prob = predict(uploaded_file)
    new_image = image.resize((300, 300))
    with col1:
        st.write("")
        st.image(new_image, caption=f'This a {(max_class).capitalize()}!', use_column_width=False)
    with col2:
        # predict(uploaded_file)
        st.subheader('Predicted class:')
        st.write(f'**{(max_class).capitalize()}** with a probability of {max_prob: .3f}')
    
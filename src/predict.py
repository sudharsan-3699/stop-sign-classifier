from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt

def predict_single(img_path, model_path='stop_sign_classifier.h5', img_height=64, img_width=64, train_generator=None):
    model = load_model(model_path)
    img = image.load_img(img_path, target_size=(img_height, img_width))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    class_idx = np.argmax(prediction)
    if train_generator:
        class_labels = list(train_generator.class_indices.keys())
    else:
        class_labels = ['not_stop', 'stop']  # fallback labels

    predicted_label = class_labels[class_idx]

    plt.imshow(img)
    plt.title(f'{img_path}: Prediction = {predicted_label}')
    plt.axis('off')
    plt.show()

    return predicted_label

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from .model import create_model

def train_model(data_dir='data', img_height=64, img_width=64, batch_size=32, epochs=10):
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=0.2
    )

    train_generator = train_datagen.flow_from_directory(
        data_dir,
        target_size=(img_height, img_width),
        batch_size=batch_size,
        class_mode='categorical',
        subset='training'
    )

    val_generator = train_datagen.flow_from_directory(
        data_dir,
        target_size=(img_height, img_width),
        batch_size=batch_size,
        class_mode='categorical',
        subset='validation'
    )

    model = create_model(img_height, img_width)
    history = model.fit(
        train_generator,
        epochs=epochs,
        validation_data=val_generator
    )
    model.save('stop_sign_classifier.h5')
    print("Model training completed and saved as stop_sign_classifier.h5")

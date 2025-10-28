Stop Sign Image Classification using CNN

Table of Contents
1. Introduction
2. Problem Statement  
3. Dataset Used  
4. Model Architecture
5. Instructions for Running the Code
6. Implementation Steps
7. Insights and Challenges  

1.Introduction  
This project demonstrates the development of a Convolutional Neural Network (CNN) for binary image classification — specifically, classifying whether an image contains a stop sign or not. The project is implemented in Python using TensorFlow/Keras and is intended as a complete demonstration of a modern deep learning workflow, from data preparation to deployment-ready prediction scripts.  

2.Problem Statement  
The task is to develop a machine learning model that can accurately distinguish between images containing stop signs and those that do not. Applications of such a system include autonomous driving, advanced driver-assistance systems (ADAS), and traffic surveillance, where robust detection of road signs is critical.  

3.Dataset Used  
Classes: Stop signs and Not Stop signs, organized into:  

    data/stop/
    data/not_stop/

Download the dataset: 

    https://drive.google.com/drive/folders/1818x1ukoJy8UHIbItOYJ_25ssh-U3gp3?usp=sharing
Instructions:  
Download and unzip the dataset.    
Place the stop and not_stop folders inside a new data/ directory at the project root.    
The final structure should be:  

    data/
      stop/
      not_stop/

4.Model Architecture  
* Framework: TensorFlow (Keras API)
* Input Size: 64x64 RGB image

* Network Layers:
  Conv2D(32, 3x3, relu) + MaxPooling2D(2x2)
  Conv2D(64, 3x3, relu) + MaxPooling2D(2x2)
  Flatten
  Dense(64, relu) + Dropout(0.5)
  Dense(2, softmax)

* Optimizer: Adam
* Loss Function: Categorical Crossentropy

5.Instructions for Running the Code
* Prerequisites
* Python 3.7+
* pip

  i. Clone the repository
  
      git clone https://github.com/sudharsan-3699/stop-sign-classifier/  
      cd stop-sign-classifier

  ii. Create and Activate a Virtual Environment
  
      python -m venv venv
      # Windows:  
        venv\Scripts\activate  
      # Mac/Linux:  
        source venv/bin/activate  

  iii. Install All Dependencies

      pip install -r requirements.txt

  iv. Add Your Data
    * Place stop sign images in data/stop/
    * Place non-stop images in data/not_stop/
    * Images should be jpg/png format.

  v. Clean the Dataset
  
      python scripts/run_clean.py

  vi. Train the Model
  
      python scripts/run_train.py

  vii. Predict on a New Image
  
      python scripts/run_predict.py path/to/test_image.jpg


6. Implementation Steps  
    * Data Preparation: Collected and organized images into separate folders (stop, not_stops).
    * Preprocessing: Cleaned images to remove corrupt files using Pillow.
    * Model Construction: Defined and tested CNN model architecture in Keras.
    * Training: Performed efficient data loading, augmentation, and training with validation monitoring.
    * Evaluation: Recorded validation performance and manually sampled prediction outputs.
    * Documentation: Provided code, usage instructions, and explanatory comments.
    * Testing: Used script to batch predict and visualize sample images.

7. Insights and Challenges
    * Data Cleaning: Some images were corrupt or incorrectly formatted, requiring an automated cleanup step.

    * Environment Management: Faced and resolved pip/venv confusion to ensure all packages installed locally.

    * Accuracy vs. Complexity: A simple CNN architecture proved effective for this binary classification task, highlighting the importance of good data, preprocessing, and clear labeling.

    * Reproducibility: The script-based project structure (no notebooks required) makes this project easy to reproduce or modify for similar image classification tasks.

    * Further Improvements: Possible enhancements include data augmentation, transfer learning, and deployment as a web API.

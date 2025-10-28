import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.preprocess import clean_and_verify_images

if __name__ == "__main__":
    data_directory = "data"
    clean_and_verify_images(data_directory)
 
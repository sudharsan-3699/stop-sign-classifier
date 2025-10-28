import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.train import train_model

if __name__ == "__main__":
    train_model(data_dir="data", img_height=64, img_width=64, epochs=10)

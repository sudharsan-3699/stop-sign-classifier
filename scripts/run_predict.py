import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.predict import predict_single
import sys

if __name__ == "__main__":
    img_path = sys.argv[1] if len(sys.argv) > 1 else None
    if img_path is None:
        print("Usage: python run_predict.py path/to/image.jpg")
        sys.exit(1)
    predict_single(img_path)

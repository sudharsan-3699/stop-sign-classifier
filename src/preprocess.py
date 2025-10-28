import os
from PIL import Image

def clean_and_verify_images(data_dir):
    for class_dir in os.listdir(data_dir):
        class_path = os.path.join(data_dir, class_dir)
        if os.path.isdir(class_path):
            for fname in os.listdir(class_path):
                fpath = os.path.join(class_path, fname)
                if os.path.isfile(fpath):
                    try:
                        img = Image.open(fpath)
                        img.verify()
                    except:
                        print(f"Corrupted: {fpath}")
                        os.remove(fpath)

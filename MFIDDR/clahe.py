import cv2
import os

def check_image_size(folder_path):
    """
    Checks the size of each image in the specified folder.

    Parameters:
        folder_path (str): Path to the folder containing images.
    """
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename.endswith('.jpg'):
            img = cv2.imread(file_path)
            if img is not None:
                height, width, _ = img.shape
                print(f"Image '{filename}' size: {width}x{height}")
            else:
                print(f"Error reading image '{filename}'")

def apply_clahe_to_images(folder_path):
    """
    Applies Contrast Limited Adaptive Histogram Equalization (CLAHE) to each image in the specified folder.

    Parameters:
        folder_path (str): Path to the folder containing images.
    """
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename.endswith('.jpg'):
            img = cv2.imread(file_path)
            if img is not None:
                img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
                l_channel, a_channel, b_channel = cv2.split(img_lab)
                l_channel_clahe = clahe.apply(l_channel)
                img_lab_clahe = cv2.merge((l_channel_clahe, a_channel, b_channel))
                img_clahe = cv2.cvtColor(img_lab_clahe, cv2.COLOR_LAB2BGR)
                cv2.imwrite(file_path, img_clahe)
                print(f"CLAHE applied to image '{filename}'")
            else:
                print(f"Error reading image '{filename}'")

# Example usage
folder_path = "./sample/copied-images"  # Replace this with the path to your folder

# Check the size of the images
print("Image Sizes:")
check_image_size(folder_path)

# Apply CLAHE to the images
apply_clahe_to_images(folder_path)

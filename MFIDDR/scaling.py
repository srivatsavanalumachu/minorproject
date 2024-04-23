from PIL import Image
import os

def scale_images_in_folder(folder_path, output_size=(512, 512)):
    """
    Scales all images in the specified folder to the given output size.

    Parameters:
        folder_path (str): Path to the folder containing images.
        output_size (tuple): Output size of the scaled images in the format (width, height).
    """
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename.endswith('.jpg'):
            try:
                img = Image.open(file_path)
                img = img.resize(output_size)
                img.save(file_path)  # Overwrite the original image with the scaled version
            except Exception as e:
                print(f"Error scaling image {filename}: {e}")

# Example usage
source_path = "./sample/copied-images"  # Replace this with the path to your folder
scale_images_in_folder(source_path)

import os
import shutil

def read_jpg_files_in_folder(path):
    """
    Reads all JPG files in the specified folder.

    Parameters:
        path (str): Path to the folder containing JPG files.

    Returns:
        dict: Dictionary containing file names as keys and file contents as values.
    """
    file_contents = {}
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path) and filename.endswith('.jpg'):
            with open(file_path, 'rb') as file:  # Use 'rb' mode for binary files like images
                file_contents[filename] = file.read()
    return file_contents

def copy_files_to_folder(file_contents, dest_folder):
    """
    Copies files from a dictionary to a destination folder.

    Parameters:
        file_contents (dict): Dictionary containing file names as keys and file contents as values.
        dest_folder (str): Path to the destination folder.
    """
    # Create the destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    # Copy each file to the destination folder
    for filename, content in file_contents.items():
        file_path = os.path.join(dest_folder, filename)
        with open(file_path, 'wb') as file:  # Use 'wb' mode for writing binary files
            file.write(content)

# Example usage
source_path = "./sample/test-examples"  # Replace this with the path to your folder
jpg_file_contents = read_jpg_files_in_folder(source_path)

destination_path = "./sample/copied-images"  # Replace this with the path to your destination folder
copy_files_to_folder(jpg_file_contents, destination_path)

import os

def get_image_files(folder_path):
    image_extensions = ('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')
    return [f for f in os.listdir(folder_path) if f.lower().endswith(image_extensions)]
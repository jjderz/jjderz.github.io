import os
from PIL import Image, UnidentifiedImageError
import pillow_heif

def convert_heic_to_jpg(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    allowed_extensions = {'.jpg', '.jpeg', '.png', '.heic'}

    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue

        file_extension = os.path.splitext(filename.lower())[1]

        if file_extension in allowed_extensions:
            if file_extension == '.heic':
                try:
                    image = Image.open(file_path)
                    jpg_file_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.jpg")
                    image.save(jpg_file_path, "JPEG")
                    print(f"Converted {filename} to {jpg_file_path}")
                except UnidentifiedImageError:
                    print(f"Could not identify image file {filename}, skipping.")
        else:
            os.remove(file_path)
            print(f"Removed {filename} (unsupported file type)")

input_folder = 'images'  # Folder containing images
output_folder = 'images/converted'  # Folder to save converted images

convert_heic_to_jpg(input_folder, output_folder)

import os

def list_jpg_files(directory):
    jpg_files = []
    for filename in os.listdir(directory):
        if filename.lower().endswith('.jpg'):
            jpg_files.append(filename)
    return jpg_files

images_folder = 'images'

jpg_files = list_jpg_files("images")
print("JPG files in the images folder:")
for jpg_file in jpg_files:
    print("'images/" + jpg_file + "',")

import os
import shutil

left_root = '../images_original'
right_flat = '../images_new'

# Get list of all image files in the right folder
right_images = {filename for filename in os.listdir(right_flat) if os.path.isfile(os.path.join(right_flat, filename))}

# Walk through the left_root folder structure
for dirpath, _, filenames in os.walk(left_root):
    for filename in filenames:
        if filename in right_images:
            left_file_path = os.path.join(dirpath, filename)
            right_file_path = os.path.join(right_flat, filename)

            # Replace the file
            shutil.copy2(right_file_path, left_file_path)
            print(f"Replaced: {left_file_path}")

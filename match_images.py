import os
import shutil
import sys

if len(sys.argv) != 3:
    print("Usage: python update_images.py <left_root_folder> <right_flat_folder>")
    sys.exit(1)

left_root = sys.argv[1]
right_flat = sys.argv[2]

# Validate paths
if not os.path.isdir(left_root):
    print(f"Error: '{left_root}' is not a valid folder.")
    sys.exit(1)

if not os.path.isdir(right_flat):
    print(f"Error: '{right_flat}' is not a valid folder.")
    sys.exit(1)

# Get list of all image files in the right folder
right_images = {filename for filename in os.listdir(right_flat) if os.path.isfile(os.path.join(right_flat, filename))}

# Walk through the left_root folder structure
replaced_count = 0
for dirpath, _, filenames in os.walk(left_root):
    for filename in filenames:
        if filename in right_images:
            left_file_path = os.path.join(dirpath, filename)
            right_file_path = os.path.join(right_flat, filename)

            # Replace the file
            shutil.copy2(right_file_path, left_file_path)
            print(f"Replaced: {left_file_path}")
            replaced_count += 1

print(f"✅ Done. {replaced_count} files replaced.")

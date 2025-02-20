import os
from PIL import Image, UnidentifiedImageError
import logging

# logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the parent directory containing the folders with pics
parent_folder = "from where to get those folder's of images"
output_parent_folder = "Where you want to save"

# Create the output parent folder if it doesn't have
os.makedirs(output_parent_folder, exist_ok=True)

# Walk through the parent folder and its subdirectories
for root, dirs, files in os.walk(parent_folder):
    # Calculate the relative path from the parent folder
    relative_path = os.path.relpath(root, parent_folder)

    # Create corresponding folder in the output directory
    output_folder = os.path.join(output_parent_folder, relative_path)
    os.makedirs(output_folder, exist_ok=True)

    # Loop through each file in the current folder
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):  # Modify extensions as needed
            img_path = os.path.join(root, file)
            try:
                # Lazy loading to avoid loading entire image in memory
                img = Image.open(img_path)
                logging.info(f"Processing file: {file}")

                # Handle large images by resizing with ANTIALIAS (or LANCZOS)
                img_resized = img.resize((256, 256), Image.LANCZOS)

                # Convert RGBA to RGB to handle JPEG format limitations
                if img.mode == 'RGBA':
                    img_resized = img_resized.convert('RGB')

                # Save the resized image in the corresponding output folder
                img_resized.save(os.path.join(output_folder, file))
            except UnidentifiedImageError:
                logging.error(f"Cannot identify image file {file}, skipping.")
            except OSError as e:
                logging.error(f"Error processing file {file}: {e}, skipping.")
            except Exception as e:
                logging.error(f"Unexpected error with file {file}: {e}, skipping.")

print("Resizing complete and folder structure replicated!")

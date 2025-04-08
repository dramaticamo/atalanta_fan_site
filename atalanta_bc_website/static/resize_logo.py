from PIL import Image
import os

# Define input and output folder paths
input_folder = "static/images/logos/"
output_folder = "static/images/logos_resized/"

# Ensure the output directory exists
os.makedirs(output_folder, exist_ok=True)

# Define the target size for logos (50x50)
TARGET_SIZE = (50, 50)

# Loop through all images in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Resize the image while maintaining aspect ratio
        img = img.resize(TARGET_SIZE, Image.ANTIALIAS)

        # Save the resized image to the output folder
        img.save(os.path.join(output_folder, filename))

print("✅ All logos resized to 50x50 successfully!")

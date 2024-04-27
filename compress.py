from PIL import Image
import os

def compress_image(input_image_path, output_image_path, target_size_mb=1):
    # Load the image
    image = Image.open(input_image_path)

    # Calculate the target size in bytes
    target_size_bytes = target_size_mb * 1024 * 1024

    # Compress the image with varying quality levels until the target size is reached
    quality = 90  # Initial quality level
    while os.path.getsize(output_image_path) > target_size_bytes and quality > 0:
        
        # Save the image with the current quality level
        image.save(output_image_path, quality=quality, optimize=True)
        
        # Decrease the quality for the next iteration
        quality -= 10

    print(f"Image compressed to approximately {os.path.getsize(output_image_path) / (1024 * 1024):.2f} MB")


# Example usage:
input_image_path = input("Enter the path to the input image: ")
output_image_path = 'processed_images/'
target_size_mb = input("Enter the target size in megabytes: ")

compress_image(input_image_path, output_image_path, target_size_mb)

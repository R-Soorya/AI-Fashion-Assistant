from PIL import Image
import os

def save_outfit_images(api_response, collections, base_folder="wardrobe_recommendation/classified_fits", output_folder=r'E:\Final Year Project\app\static\weekly_outfits'):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Loop through each day's outfit in the API response
    for day, outfit in api_response.items():
        # Find the top and bottom image filenames based on the outfit plan
        top_filename = next(item['filename'] for item in collections['top'] if item['filename'].split('.')[0] == outfit['top'].replace(' ', '_').lower())
        bottom_filename = next(item['filename'] for item in collections['bottom'] if item['filename'].split('.')[0] == outfit['bottom'].replace(' ', '_').lower())

        # Load images from the classified_fits directory
        top_img_path = os.path.join(base_folder, "top", top_filename)
        bottom_img_path = os.path.join(base_folder, "bottom", bottom_filename)

        top_img = Image.open(top_img_path)
        bottom_img = Image.open(bottom_img_path)

        # Resize images to have the same height
        max_height = max(top_img.height, bottom_img.height)
        top_img = top_img.resize((int(top_img.width * max_height / top_img.height), max_height))
        bottom_img = bottom_img.resize((int(bottom_img.width * max_height / bottom_img.height), max_height))

        # Combine images side by side
        combined_width = top_img.width + bottom_img.width
        combined_img = Image.new("RGB", (combined_width, max_height), (255, 255, 255))
        combined_img.paste(top_img, (0, 0))
        combined_img.paste(bottom_img, (top_img.width, 0))

        # Save the combined image for the day
        combined_img.save(os.path.join(output_folder, f"outfit_{day.replace(' ', '_').lower()}.jpg"))
        print(f"Saved: {output_folder}/outfit_{day.replace(' ', '_').lower()}.jpg")


# save_outfit_images(api_response, collections)


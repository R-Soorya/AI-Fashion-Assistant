from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import torch
import os
import shutil
from wardrobe_recommendation import color_detection

def save_collections():
    # Load the processor and model from the local directory
    local_model_path = r"E:\Final Year Project\app\wardrobe_recommendation\classification_model"
    processor = AutoImageProcessor.from_pretrained(local_model_path)
    model = AutoModelForImageClassification.from_pretrained(local_model_path)

    # Load class labels
    labels = model.config.id2label

    # Define source and target directories
    source_dir = r"E:\Final Year Project\app\wardrobe_recommendation\collections"
    top_dir = r"E:\Final Year Project\app\wardrobe_recommendation\classified_fits\top"
    bottom_dir = r"E:\Final Year Project\app\wardrobe_recommendation\classified_fits\bottom"

    # Initialize dictionary to store classified images and counters
    classified_images = {"top": [], "bottom": []}
    top_counters = {}
    bottom_counters = {}

    # Clear target directories if they contain any files
    for dir_path in [top_dir, bottom_dir]:
        if os.path.exists(dir_path):
            for file in os.listdir(dir_path):
                file_path = os.path.join(dir_path, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)

    # Create target directories if they don't exist
    os.makedirs(top_dir, exist_ok=True)
    os.makedirs(bottom_dir, exist_ok=True)

    # Define categories for top fits and bottom fits
    top_categories = ["T - shirt / top", "Shirt", "Pullover", "Coat"]
    bottom_categories = ["Trouser"]

    # Process each image in the "collections" folder
    for filename in os.listdir(source_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(source_dir, filename)
            
            # Open and preprocess the image
            image = Image.open(image_path)
            inputs = processor(images=image, return_tensors="pt")
            
            # Get model predictions
            with torch.no_grad():
                outputs = model(**inputs)
                logits = outputs.logits
                predicted_class_idx = logits.argmax(-1).item()
            
            # Determine label and destination directory
            predicted_label = labels[predicted_class_idx]

            # Get the color of the costume using the color function
            detected_color = color_detection.color(image_path)  # This should return an RGB tuple

            if any(top_item in predicted_label for top_item in top_categories):
                dest_dir = top_dir
                category_name = predicted_label.lower().replace(' ', '_').replace('/', '-')  # Replace '/' with '-' for filename safety
                if category_name not in top_counters:
                    top_counters[category_name] = 0
                top_counters[category_name] += 1
                new_filename = f"{category_name}_{top_counters[category_name]}.jpg"
                classified_images['top'].append({
                    "filename": new_filename,
                    "color": detected_color  # Save the detected color
                })

            elif any(bottom_item in predicted_label for bottom_item in bottom_categories):
                dest_dir = bottom_dir
                category_name = predicted_label.lower().replace(' ', '_').replace('/', '-')  # Replace '/' with '-' for filename safety
                if category_name not in bottom_counters:
                    bottom_counters[category_name] = 0
                bottom_counters[category_name] += 1
                new_filename = f"{category_name}_{bottom_counters[category_name]}.jpg"
                classified_images['bottom'].append({
                    "filename": new_filename,
                    "color": detected_color  # Save the detected color
                })

            else:
                print('Unable to predict',predicted_label)
                print('Unable to detect',filename)

            # Save file to the appropriate directory with the new filename
            shutil.copy(image_path, os.path.join(dest_dir, new_filename))
            print(f"Image '{filename}' classified as '{predicted_label}' with color {detected_color} and saved as '{new_filename}' in '{dest_dir}'.")
    
    print("Classification and saving process completed.")
    print("Classified images:\n", classified_images)

    return classified_images




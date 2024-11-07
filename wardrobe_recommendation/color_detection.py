import cv2
from sklearn.cluster import KMeans

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))  # Resize to the model's input size
    return img

def get_dominant_color(image):
    pixels = image.reshape(-1, 3)
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(pixels)
    dominant_color = kmeans.cluster_centers_  # Get the most dominant color
    return tuple(dominant_color.astype(int))  # Return as RGB tuple

import requests

def get_color_name_from_api(r,g,b):
    # API URL (this is an example, check the documentation for any specific API you want to use)
    url = f'https://www.thecolorapi.com/id?rgb=rgb({r},{g},{b})'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        color_name = data['name']['value']
        return color_name
    else:
        return "Color name not found"

# Example RGB color
# rgb_color = (60,  80, 116)  # Replace with your RGB value
# color_name = get_color_name_from_api(122,110, 94)
# print(f"The color name for {rgb_color} is: {color_name}")

def color(image_path):
    # Preprocess the image
    res = preprocess_image(image_path)
    
    # Get the dominant colors
    colors = get_dominant_color(res)
    
    # Extract the second color (colors[1])
    r, g, b = colors[1]
    
    # Call the API to get the color name
    color_name = get_color_name_from_api(r, g, b)
    
    # Print the result
    # print(f"The color name for the dominant color {colors[1]} is: {color_name}")
    return color_name

    



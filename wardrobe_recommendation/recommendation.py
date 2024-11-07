
from wardrobe_recommendation import classification, prompt, pairs
import google.generativeai as genai
import json

genai.configure(api_key="AIzaSyDB9Xerpu6YhwejJsUVmZsUVmLV1RB8lsk")
model = genai.GenerativeModel("gemini-1.5-flash")

def recommend():
    collections = classification.save_collections()

    print("Classified Collections:\n")
    for category, items in collections.items():
        print(f"{category.capitalize()}:")
        for item in items:
            print(f"  - Filename: {item['filename']}, Color: {item['color']}")
        print()

    prompt_ = prompt.generate_prompt(collections)
    refined_prompt = [
        {
            'role': 'user',
            'parts': [prompt_]
        }
    ]
    response = model.generate_content(refined_prompt)
    cleaned_response = json_response(response)

    print('Json Response:\n',cleaned_response,'\n')

    pairs.save_outfit_images(cleaned_response, collections)

def json_response(response):
    # Remove the marker
    formatted_string = response.text.splitlines()[1:-1]  # Skip the first line (marker)
    cleaned_response = '\n'.join(formatted_string).strip()

    # Wrap the content in curly braces to make it a valid JSON object
    cleaned_response = '{' + cleaned_response + '}'

    # Ensure the keys are properly formatted (removes extra quotes)
    cleaned_response = cleaned_response.replace('""day', '"day')

    # Remove trailing commas if present
    cleaned_response = cleaned_response.replace(",}", "}")

    print("Cleaned Response:\n", cleaned_response, '\n')

    # Parse the cleaned_response string to a dictionary
    try:
        # Assuming cleaned_response is a JSON string
        api_response = json.loads(cleaned_response)
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        api_response = {}
    
    return api_response

# collections = {'top': [{'filename': 'shirt_1.jpg', 'color': 'Cloud Burst'}, {'filename': 'shirt_2.jpg', 'color': 'Gray Nurse'}, {'filename': 'shirt_3.jpg', 'color': 'Pigeon Post'}, {'filename': 'shirt_4.jpg', 'color': 'Van Cleef'}, {'filename': 'shirt_5.jpg', 'color': 'Desert Storm'}], 'bottom': [{'filename': 'trouser_1.jpg', 'color': 'Indian Khaki'}, {'filename': 'trouser_2.jpg', 'color': 'Dune'}, {'filename': 'trouser_3.jpg', 'color': 'Eerie Black'}]}


# regenerate_prompt = prompt.regeneration_prompt(collections)








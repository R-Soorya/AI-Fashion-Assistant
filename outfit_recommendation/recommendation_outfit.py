import google.generativeai as genai
import json
from outfit_recommendation import prompt

genai.configure(api_key="AIzaSyD-dGFRJp45jnTHXDzDXf6P46Bok7ZsoX0")

model = genai.GenerativeModel("gemini-1.5-flash")

def json_response(response):
    # Remove the marker
    formatted_string = response.text.splitlines()[1:-1]  # Skip the first line (marker)
    cleaned_response = '\n'.join(formatted_string).strip()

    # Create a valid JSON array
    cleaned_response = '[' + cleaned_response + ']'

    # Remove trailing commas if present
    cleaned_response = cleaned_response.replace(",]", "]")  # Removes trailing comma before closing bracket

    # print("Cleaned Response:\n", cleaned_response, '\n')

    # Parse the cleaned_response string to a list of dictionaries
    try:
        api_response = json.loads(cleaned_response)
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        api_response = []
    return api_response

def generate_suggestions(preference):

    # preference = {'gender' : 'male',
    #             'face_shape' : 'oval',
    #             'body_shape' : 'rectangle',
    #             'skin_tone' : 'fair',
    #             'height' : 'average',
    #             'dress_type' : 'formals'}

    
    # prompt_ = prompt.generate_prompt(preference)

    print(preference)

    
    if preference['gender'] == 'men' and preference['dress_type'] == 'festival_wear':
        prompt_ = prompt.generate_prompt_men_festival(preference)
    elif preference['gender'] == 'men' and preference['dress_type'] == 'casuals':
        prompt_ = prompt.generate_prompt_men_casual(preference)
    elif preference['gender'] == 'women' and preference['dress_type'] == 'festival_wear':
        prompt_ = prompt.generate_prompt_women_festival(preference)
    elif preference['gender'] == 'men':
        prompt_ = prompt.generate_prompt_men(preference)
    else:
        prompt_= prompt.generate_prompt_women(preference)

    refined_prompt = [
        {
            'role': 'user',
            'parts': [prompt_]
        }
    ]

    response = model.generate_content(refined_prompt)

    # print('\nResponse:',response.text)

    jsonresponse = json_response(response)

    return jsonresponse


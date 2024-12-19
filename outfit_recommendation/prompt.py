
def generate_prompt_men(preference):

    print('--------------------------------------------\nGenerating outfit for men')
    prompt = f"""

Generate a list of 5   {preference['dress_type']} outfit combinations for a {preference['gender']}, {preference['body_shape']} body shape, {preference['skin_tone']} skin tone, and {preference['height']} height.
Each outfit should focus on pairing colors thoughtfully to create a polished, professional look.
Consider options like well-matched suits, shirts, trousers, using color combinations that highlight the skin tone and complement the face and body shape.
Ensure each suggestion balances style with classic, sophisticated formality suitable for various professional settings.
It should focus more on fomal dress

The output should be structured in JSON format, adhering strictly to the following guidelines:

Output format:
    {{ "shirt 1" : "pant 1" }},
    {{ "shirt 2" : "pant 2" }},
    {{ "shirt 3" : "pant 3" }}

Generate a list of 6 pairs of well and good combination of outfit.
Each shirt name should also clearly indicate the shirt and color (e.g., "pale pink shirt").
Each pant name should also clearly indicate the pant and color (e.g., "charcoal gray pant").
There should not be any brand name (e.g., "oxford" )
If it is a casual wear you can aslo suggest t-shirt or any kind of casual dress that is in trend and best suited for girls.
Make sure that there should not be any brand
    
Ensure that the color combinations are well-coordinated and suitable for a classic, sophisticated formal setting.
The outfit pairings should be easy for the user to understand and follow for a stylish and professional look.

There should not be more than 5 suggestions.
The output should be in the above json format. There should not be any other extra content like explanation.
Ensure that there are no additional explanations or content outside of the JSON structure.

    """
    return prompt

def generate_prompt_women(preference):
    print('--------------------------------------------\nGenerating outfit for women')
    prompt = f"""

Generate a list of 5 {preference['dress_type']} outfit combinations for a {preference['gender']}, {preference['body_shape']} body shape, {preference['skin_tone']} skin tone, and {preference['height']} height.
Each outfit should focus on pairing colors thoughtfully to create a polished, trendy, and stylish look.
Consider options like jeans, t-shirts, churidars, tops, skirts, dresses, trousers, or any other trendy styles appropriate for girls and aligned with the specified dress type.
Use color combinations that highlight the skin tone and complement the face and body shape.

The output should strictly follow this format:
    {{ "top description": "bottom description" }},
    {{ "top description": "bottom description" }},
    {{ "top description": "bottom description" }}

For example:
    {{ "cream-colored ribbed knit top": "light wash high-waisted skinny jeans" }},
    {{ "olive green oversized button-down shirt": "dark brown corduroy mini skirt" }},
    {{ "pastel yellow puff-sleeve blouse": "white high-waisted tailored trousers" }}

Make sure that this is only the example, the content of the  response should not be the same as above.
Each "top description" should clearly describe the type and color of the top (e.g., "white graphic t-shirt", "navy cotton kurta").
Each "bottom description" should clearly describe the type and color of the bottom (e.g., "blue high-waisted jeans", "black leggings").
Ensure the color combinations are well-coordinated, stylish, and suitable for the specified dress type.
Avoid any mention of brand names (e.g., "Nike", "Levi's").

Ensure that all suggestions reflect current trends and are appropriate for the given preferences in {preference['dress_type']}.
The output should strictly follow the JSON format with no additional explanation or content outside of the JSON structure.

There should not be more than 5 suggestions.

    """
    return prompt


def generate_prompt_women_festival(preference):
    print('--------------------------------------------\nGenerating outfit for women(festival)')
    
    prompt = f"""

Generate a list of 5 {preference['dress_type']} outfit combinations for a {preference['gender']}, {preference['body_shape']} body shape, {preference['skin_tone']} skin tone, and {preference['height']} height.
Each outfit should focus on pairing colors thoughtfully to create a polished, trendy, and stylish look.
Consider options like sarees, lehengas, anarkalis, salwar suits, kurtis, skirts, and other traditional or semi-traditional styles that reflect the festive spirit.
Use color combinations that highlight the skin tone and complement the face and body shape.

The output should strictly follow this format:
    {{ "top description": "bottom description" }},
    {{ "top description": "bottom description" }},
    {{ "top description": "bottom description" }}

For example:
    {{ "royal blue embellished kurti": "golden embroidered palazzo pants" }},
    {{ "maroon silk blouse": "cream handwoven saree" }},
    {{ "peach netted anarkali top": "matching churidar leggings" }}

Make sure that this is only the example, the content of the  response should not be the same as above.
Each "top description" should clearly describe the type and color of the top (e.g., "royal blue embellished kurti", "maroon silk blouse").
Each "bottom description" should clearly describe the type and color of the bottom (e.g., "golden embroidered palazzo pants", "cream handwoven saree").
Use color combinations that highlight the skin tone, complement the face and body shape, and evoke the festive atmosphere.

Ensure that all suggestions reflect current trends and are appropriate for the given preferences in {preference['dress_type']}.
The output should strictly follow the JSON format with no additional explanation or content outside of the JSON structure.

There should not be more than 5 suggestions.

    """
    return prompt


def generate_prompt_men_festival(preference):
    print('--------------------------------------------\nGenerating outfit for men(festival)')
    prompt = f"""

Generate a list of 5 {preference['dress_type']} outfit combinations for a {preference['gender']}, {preference['body_shape']} body shape, {preference['skin_tone']} skin tone, and {preference['height']} height.
Each outfit should focus on pairing colors thoughtfully to create a polished, trendy, and stylish look.
Consider options like veshtis, mundus, kurta sets, angavastram, sherwanis, traditional shirts, or other regional styles popular in Tamil Nadu and Kerala that reflect the festive and cultural spirit.
Use color combinations that highlight the skin tone and complement the face and body shape.

The output should strictly follow this format:
    {{ "top description": "bottom description" }},
    {{ "top description": "bottom description" }},
    {{ "top description": "bottom description" }}

For example:
    {{ "white cotton kurta with gold embroidery": "matching cream cotton veshti" }},
    {{ "dark blue silk kurta with subtle patterns": "gold-bordered white veshti" }},
    {{ "light green traditional angavastram": "matching cream-colored veshti" }}

Make sure that this is only the example, the content of the response should not be the same as above.
Each "top description" should clearly describe the type and color of the top (e.g., "white cotton kurta with gold embroidery", "dark blue silk kurta").
Each "bottom description" should clearly describe the type and color of the bottom (e.g., "matching cream cotton veshti", "gold-bordered white mundu").
Use color combinations that highlight the skin tone, complement the face and body shape, and evoke the festive atmosphere.
Dont add the word mundu, instead of that add veshti

Ensure that all suggestions reflect current trends and are appropriate for the given preferences in {preference['dress_type']}.
The output should strictly follow the JSON format with no additional explanation or content outside of the JSON structure.

There should not be more than 5 suggestions.

    """
    return prompt


def generate_prompt_men_casual(preference):
    print('--------------------------------------------\nGenerating outfit for men(casual)')
    
    prompt = f"""

Generate a list of 5 {preference['dress_type']} outfit combinations for a {preference['gender']}, {preference['body_shape']} body shape, {preference['skin_tone']} skin tone, and {preference['height']} height.
Each outfit should focus on pairing colors thoughtfully to create a polished, trendy, and stylish look suitable for boys.
Consider options like casual shirts, t-shirts, denim jackets, hoodies, jeans, chinos, shorts, or other trendy styles appropriate for boys and aligned with the specified dress type.
Use color combinations that highlight the skin tone and complement the face and body shape.

The output should strictly follow this format:
    {{ "top description": "bottom description" }},
    {{ "top description": "bottom description" }},
    {{ "top description": "bottom description" }}

For example:
    {{ "navy blue graphic t-shirt": "dark wash slim-fit jeans" }},
    {{ "white casual button-up shirt": "khaki chinos" }},
    {{ "grey hoodie with subtle prints": "black jogger pants" }}

Make sure that this is only the example, the content of the response should not be the same as above.
Each "top description" should clearly describe the type and color of the top (e.g., "navy blue casual t-shirt", "white button-up shirt").
Each "bottom description" should clearly describe the type and color of the bottom (e.g., "dark wash slim-fit jeans", "black jogger pants").
Ensure the color combinations are well-coordinated, stylish, and suitable for the specified dress type.
Avoid any mention of brand names (e.g., "Nike", "Levi's").

Ensure that all suggestions reflect current trends for boys and are appropriate for the given preferences in {preference['dress_type']}.
The output should strictly follow the JSON format with no additional explanation or content outside of the JSON structure.

There should not be more than 5 suggestions.

    """
    return prompt







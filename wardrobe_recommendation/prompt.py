
def generate_prompt(collections):

    # Generate the formatted wardrobe details without .jpg extension
    top_details = "\n".join([f"{i+1}.  {item['filename'].split('.')[0].capitalize().replace('_', ' ')}: {item['color']}" 
                              for i, item in enumerate(collections['top'])])
    bottom_details = "\n".join([f"{i+1}.  {item['filename'].split('.')[0].capitalize().replace('_', ' ')}: {item['color']}" 
                                 for i, item in enumerate(collections['bottom'])])

    # Define the main prompt structure
    prompt = f"""
Create a weekly outfit plan using the provided wardrobe collection, ensuring that each pairing is stylish, trendy, and color-coordinated.
Each outfit should consist of one top and one bottom, carefully chosen to provide a balanced mix of casual and semi-formal styles, making each day’s outfit unique and visually appealing.

Key Focus Areas:

**Focus on Neutral colours:**
The basic of any fashion is to focus on neutral colours because those colourswill make other colours prominent.
So, when it comes to wearing neutral colours,always have at least one base in your overall outfits like wearing a base layer of neutral colour when you are wearing a blazer on it or a neutral T-shirt for dark  pants and shoes.
Neutral colours like white, grey, sky blue, and khaki will be veryattractive on any occasion for men. These are the colours that go with other colours, this is the base foundation for any outfits and carry outstanding stylingessence around.

**Enhanced Color Harmony:** Prioritize color combinations that complement each other beautifully or create interesting contrasts for an elevated look. Use contemporary color trends, such as earthy tones, soft pastels, and vibrant accents, to add variety and appeal. Pair colors thoughtfully—like beige with navy or olive with cream—to ensure each outfit looks sophisticated and cohesive.

**Trendy and Cohesive Combinations:** Use popular color schemes to create a stylish and modern wardrobe plan. Try monochromatic pairings for a sleek look or contrasting hues for a bold statement. Employ color schemes such as complementary or analogous palettes to make each day’s outfit unique. Consider popular color pairings like muted greens with neutrals or bold colors like burgundy with lighter shades for a refreshing contrast.

**Occasion-Specific Variety:** Curate a balance between casual looks for relaxed days and semi-formal outfits for a polished appearance. Ensure that the color combinations provide a cohesive flow throughout the week, adding freshness and a sense of style to each day’s outfit.

Objective: Generate a weekly outfit plan that goes beyond basic matching, focusing on highly appealing color combinations to elevate each look. Each day’s outfit should feature a thoughtfully selected color pairing that enhances the overall look, aligned with the latest trends for a modern and stylish appearance.

Wardrobe details:

**Tops:**
{top_details}

**Bottoms:**
{bottom_details}

Generate a 5-day outfit plan.

The response should be strictly in the below mention json format.
Output format:
{{
    day 1: {{top: top name, bottom: bottom name}},
    day 2: {{top: top name, bottom: bottom name}},
    day 3: {{top: top name, bottom: bottom name}},
    day 4: {{top: top name, bottom: bottom name}},
    day 5: {{top: top name, bottom: bottom name}}
}}

The top name should be the shirt name like Shirt 1 and not the color of the shirt.
The bottom name should be the pant name like Trouser 1 and not the color of the shirt.

Ensure that the color combinations are well-coordinated and suitable for a classic, sophisticated formal setting.

The output should be in the json format. There should not be any other extra content like explanation.
Ensure that there are no additional explanations or content outside the JSON structure.
"""

    # Print the final prompt to verify formatting
    # print(prompt)
    return prompt

def regeneration_prompt(previous_plan, collections):

    # Generate the formatted wardrobe details without .jpg extension
    top_details = "\n".join([f"{i+1}. {item['filename'].split('.')[0].capitalize().replace('_', ' ')}: {item['color']}" 
                              for i, item in enumerate(collections['top'])])
    bottom_details = "\n".join([f"{i+1}. {item['filename'].split('.')[0].capitalize().replace('_', ' ')}: {item['color']}" 
                                 for i, item in enumerate(collections['bottom'])])

    # Define the prompt structure for regenerating suggestions
    prompt = f"""
You previously generated a weekly outfit plan as follows:

{previous_plan}

Regenerate a new weekly outfit plan using the provided wardrobe collection, carefully selecting one top and one bottom for each day.
Each pairing should showcase a stylish, polished look with an emphasis on excellent color coordination and aesthetic appeal, ensuring that this plan surpasses the previous one.

Focus on:

**High-Quality Color Combinations:** Curate outfits that blend colors harmoniously or use striking contrasts to enhance each day’s look. Consider popular, fashionable palettes—such as deep tones paired with neutrals or pastels with vibrant accents—for added sophistication.
**Elevated Style Choices:** Aim for a range of styles, from casual elegance to semi-formal sophistication, incorporating creative elements that reflect modern trends. Use classic color contrasts (e.g., charcoal with cream, olive with beige) to elevate each pairing.
**Distinctive, Unique Looks:** Ensure each day offers a fresh, unique look, avoiding repetitive styles or colors. Prioritize outfits that feel cohesive while bringing out the best in each piece.
**Improved Pairings:** Ensure each top and bottom pairing creates a balanced, fashionable silhouette, highlighting in a way that enhances the overall look without clashing.
Generate a plan that demonstrates careful consideration in color and style, delivering an improved, well-coordinated outfit plan that surpasses the previous version in quality and appeal.

Wardrobe details:

**Tops:**
{top_details}

**Bottoms:**
{bottom_details}

Generate a new 5-day outfit plan with improved pairings.

The response should be strictly in the below format.
Output format:
{{
    day 1: {{top: top name, bottom: bottom name}},
    day 2: {{top: top name, bottom: bottom name}},
    day 3: {{top: top name, bottom: bottom name}},
    day 4: {{top: top name, bottom: bottom name}},
    day 5: {{top: top name, bottom: bottom name}}
}}
"""

    # Print the final prompt to verify formatting
    # print(prompt)
    return prompt


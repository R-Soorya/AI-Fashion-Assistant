from flask import Flask, render_template, request, jsonify, url_for
from outfit_recommendation import recommendation_outfit, color_generator
from wardrobe_recommendation import recommendation
import os

app = Flask(__name__)

UPLOAD_FOLDER = r'E:\Final Year Project\app\wardrobe_recommendation\collections'
WEEKLY_OUTFITS_DIR = r'E:\Final Year Project\app\static\weekly_outfits'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Home page route
@app.route('/')
def home():
    return render_template('home.html')  # Render the home page template

# Dress page route (handles both GET and POST)
@app.route('/dress', methods=['GET', 'POST'])
def dress():
    if request.method == 'POST':
        # Get data from form inputs
        gender = request.form.get('gender')
        body_shape = request.form.get('body_shape')
        skin_tone = request.form.get('skin_tone')
        height = request.form.get('height')
        dress_type = request.form.get('dress_type')

        # Prepare preference dictionary
        preference = {
            'gender': gender,
            'body_shape': body_shape,
            'skin_tone': skin_tone,
            'height': height,
            'dress_type': dress_type
        }

        # Generate suggestions based on preference
        response = recommendation_outfit.generate_suggestions(preference)

        final_response = []
        for item in response:
            capitalized_item = {}
            for key, value in item.items():
                capitalized_item[key.title()] = value.title()
            final_response.append(capitalized_item)

        print('Final response:',final_response)

        color_generator.generate_color_image(final_response)


        # Render the dress template with recommendations and passed form values
        return render_template('dress.html', final_response=final_response, 
                               gender=gender, body_shape=body_shape, skin_tone=skin_tone,
                               height=height, dress_type=dress_type)
    
    # If the request method is GET, render the dress page without recommendations
    return render_template('dress.html')


# Wardrobe page route
@app.route('/wardrobe', methods=['POST', 'GET'])
def wardrobe():
    if request.method == 'POST':

        # Ensure directories exist
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)   

        # Check if the form has the file part
        if 'wardrobeImages' not in request.files:
            return jsonify({"message": "No file part"}), 400

        files = request.files.getlist('wardrobeImages') 
        if not files:
            return jsonify({"message": "No files selected"}), 400

        # Save each file
        for file in files:
            if file.filename == '':
                return jsonify({"message": "No selected file"}), 400

            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            try:
                file.save(filepath)
                print(f"File saved to {filepath}")  # Debugging statement
            except Exception as e:
                return jsonify({"message": f"Error saving file: {str(e)}"}), 500
        
        return jsonify({"message": "Files uploaded successfully!"}), 200

    return render_template('wardrobe.html')



# Generate plan route
@app.route('/generate_plan', methods=['GET'])
def generate_plan():
    # Clear out the weekly outfits directory
    if os.path.exists(WEEKLY_OUTFITS_DIR):
        for filename in os.listdir(WEEKLY_OUTFITS_DIR):
            file_path = os.path.join(WEEKLY_OUTFITS_DIR, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
    
    # Example function to save images to weekly outfits (replace with your logic)
    recommendation.recommend()

    return jsonify({"message": "Weekly outfit plan generated and saved!"})


# Display images from weekly outfits
@app.route('/get_weekly_outfits', methods=['GET'])
def get_weekly_outfits():
    image_urls = []
    for filename in os.listdir(WEEKLY_OUTFITS_DIR):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_url = url_for('static', filename=f'weekly_outfits/{filename}')
            image_urls.append(img_url)
    
    return jsonify(image_urls)


if __name__ == '__main__':
    app.run(debug=True)

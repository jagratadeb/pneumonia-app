from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import torch
import torch.nn as nn
from torchvision import transforms, models
import io
import base64

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Load model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Define the same model architecture
model = models.resnet18(weights=None)
model.fc = nn.Linear(model.fc.in_features, 2)

# Load the trained weights
model.load_state_dict(torch.load('viral_pneumonia_model.pth', map_location=device))
model.to(device)
model.eval()

# Define the same transforms used during training
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5],
                         std=[0.5, 0.5, 0.5])
])

def predict_image(image):
    """
    Predict if an image shows Viral Pneumonia or not
    Returns: (prediction_label, confidence_score)
    """
    # Convert to RGB if needed
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Apply transforms
    image_tensor = transform(image).unsqueeze(0).to(device)
    
    # Get prediction
    with torch.no_grad():
        output = model(image_tensor)
        probabilities = torch.nn.functional.softmax(output, dim=1)
        confidence, predicted = torch.max(probabilities, 1)
    
    prediction_label = "Viral Pneumonia" if predicted.item() == 1 else "Normal/Other"
    confidence_score = confidence.item() * 100
    
    # Get both class probabilities
    prob_other = probabilities[0][0].item() * 100
    prob_viral = probabilities[0][1].item() * 100
    
    return {
        'prediction': prediction_label,
        'confidence': round(confidence_score, 2),
        'probabilities': {
            'Normal/Other': round(prob_other, 2),
            'Viral Pneumonia': round(prob_viral, 2)
        }
    }

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'model_loaded': True})

@app.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint to predict pneumonia from uploaded images
    Accepts: multipart/form-data with one or more image files
    Returns: JSON with predictions for each image
    """
    try:
        if 'images' not in request.files:
            return jsonify({'error': 'No images provided'}), 400
        
        files = request.files.getlist('images')
        
        if len(files) == 0:
            return jsonify({'error': 'No images provided'}), 400
        
        results = []
        
        for file in files:
            if file.filename == '':
                continue
                
            # Read image
            image_bytes = file.read()
            image = Image.open(io.BytesIO(image_bytes))
            
            # Get prediction
            result = predict_image(image)
            result['filename'] = file.filename
            
            # Convert image to base64 for display (optional)
            image.thumbnail((300, 300))  # Resize for display
            buffered = io.BytesIO()
            image.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            result['image_preview'] = f"data:image/png;base64,{img_str}"
            
            results.append(result)
        
        return jsonify({
            'success': True,
            'count': len(results),
            'results': results
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting Pneumonia Detection Server...")
    print(f"Using device: {device}")
    print("Model loaded successfully!")
    app.run(debug=True, host='0.0.0.0', port=5000)




@app.route('/predict', methods=['POST'])
def predict():
    """
    API endpoint to receive an image (base64 or file upload),
    run prediction, and return JSON response.
    """
    if 'file' in request.files:
        # Case 1: Image uploaded as a file
        file = request.files['file']
        image = Image.open(file.stream)
    else:
        # Case 2: Image sent as base64 string in JSON
        data = request.get_json()
        image_data = data.get('image')
        image_bytes = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(image_bytes))

    result = predict_image(image)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)

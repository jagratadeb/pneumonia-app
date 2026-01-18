# Pneumonia Detection AI - Frontend Application

A beautiful, interactive web application for detecting viral pneumonia from chest X-ray images using deep learning.

## 🎯 Features

- ✨ Clean and modern UI with drag-and-drop support
- 📤 Upload single or multiple X-ray images
- 🤖 Real-time AI predictions using ResNet18
- 📊 Confidence scores and probability breakdowns
- 🎨 Visual results with color-coded predictions
- 📱 Responsive design for all devices

## 🏗️ Architecture

- **Backend**: Flask REST API with PyTorch
- **Frontend**: React (vanilla, no build required)
- **Model**: ResNet18 trained on COVID-19 Radiography Database
- **Input**: 224x224 RGB chest X-ray images
- **Output**: Binary classification (Viral Pneumonia vs Normal/Other)

## 📋 Prerequisites

- Python 3.8 or higher
- Your trained model file: `viral_pneumonia_model.pth`
- Modern web browser (Chrome, Firefox, Safari, Edge)

## 🚀 Setup Instructions

### Step 1: Install Python Dependencies

```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install flask flask-cors torch torchvision Pillow
```

### Step 2: Place Your Model File

Copy your `viral_pneumonia_model.pth` file to the project directory:

```
project-folder/
├── app.py
├── index.html
├── requirements.txt
├── viral_pneumonia_model.pth  ← Place your .pth file here
└── README.md
```

### Step 3: Start the Backend Server

```bash
python app.py
```

You should see:
```
Starting Pneumonia Detection Server...
Using device: cpu (or cuda if GPU available)
Model loaded successfully!
 * Running on http://0.0.0.0:5000
```

### Step 4: Open the Frontend

Open `index.html` in your web browser:

- **Option 1**: Double-click `index.html`
- **Option 2**: Right-click → Open with → Your browser
- **Option 3**: Drag and drop into browser window

## 📖 How to Use

1. **Upload Images**:
   - Click the upload area to select files
   - Or drag and drop X-ray images directly
   - You can upload multiple images at once

2. **Analyze**:
   - Click "Analyze" button
   - Wait for AI processing (usually 1-2 seconds per image)

3. **View Results**:
   - Red cards indicate "Viral Pneumonia" detected
   - Green cards indicate "Normal/Other"
   - Check confidence scores and probability breakdowns

4. **Clear and Repeat**:
   - Click "Clear All" to start over
   - Upload new images for analysis

## 🔧 Configuration

### Change Backend Port

Edit `app.py` (last line):
```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Change 5000 to desired port
```

Then update `index.html` (line ~403):
```javascript
const API_URL = 'http://localhost:5000';  // Update port here too
```

### Adjust Model Confidence Threshold

In `app.py`, modify the `predict_image` function to add custom thresholds if needed.

## 🧪 Testing the Setup

1. Start the backend: `python app.py`
2. Test the health endpoint:
   ```bash
   curl http://localhost:5000/health
   ```
   Should return: `{"status":"healthy","model_loaded":true}`

3. Open the frontend and upload a test X-ray image

## 📊 Model Information

- **Architecture**: ResNet18 (no pretrained weights)
- **Training Data**: COVID-19 Radiography Database
- **Classes**: 
  - Class 0: Normal/Other (Normal, COVID, Lung Opacity)
  - Class 1: Viral Pneumonia
- **Input Size**: 224x224 pixels
- **Normalization**: mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]

## ⚠️ Important Notes

1. **Medical Disclaimer**: This tool is for research and educational purposes only. It should NOT be used for actual medical diagnosis. Always consult qualified healthcare professionals.

2. **Image Requirements**: 
   - Chest X-ray images (frontal view preferred)
   - Common formats: JPG, PNG, JPEG
   - Clear, properly exposed images work best

3. **Model Limitations**:
   - Trained specifically for viral pneumonia detection
   - May not generalize to all X-ray conditions
   - Performance depends on image quality

## 🐛 Troubleshooting

### Backend Won't Start

- **Error**: "No module named 'flask'"
  - **Solution**: `pip install flask flask-cors`

- **Error**: "No module named 'torch'"
  - **Solution**: `pip install torch torchvision`

- **Error**: "Can't find viral_pneumonia_model.pth"
  - **Solution**: Ensure the .pth file is in the same directory as app.py

### Frontend Issues

- **CORS Error**: Make sure flask-cors is installed and the backend is running
- **Predictions Not Working**: Check browser console (F12) for error messages
- **Images Not Uploading**: Ensure file format is supported (JPG, PNG, JPEG)

### Model Performance

- **Low Accuracy**: 
  - Ensure images are chest X-rays
  - Check image quality and resolution
  - Verify the .pth file matches your trained model

## 🔒 Security Notes

- This is a development setup, not production-ready
- For production:
  - Use HTTPS
  - Add authentication
  - Implement rate limiting
  - Add input validation
  - Use environment variables for configuration

## 📝 API Documentation

### POST /predict

Upload one or more images for prediction.

**Request**:
```
Content-Type: multipart/form-data
Body: images (one or more files)
```

**Response**:
```json
{
  "success": true,
  "count": 2,
  "results": [
    {
      "filename": "xray1.jpg",
      "prediction": "Viral Pneumonia",
      "confidence": 87.45,
      "probabilities": {
        "Normal/Other": 12.55,
        "Viral Pneumonia": 87.45
      },
      "image_preview": "data:image/png;base64,..."
    }
  ]
}
```

### GET /health

Check if the server is running and model is loaded.

**Response**:
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

## 🎨 Customization

### Change Color Scheme

Edit the CSS in `index.html`:
- Primary gradient: `.header` and `.button` classes
- Result cards: `.result-card.viral` and `.result-card.normal`
- Confidence bars: `.confidence-fill.viral` and `.confidence-fill.normal`

### Modify UI Text

Search and replace text in `index.html`:
- Header title: Line ~55
- Upload instructions: Lines ~388-393
- Result labels: Lines ~550-551

## 📦 Project Structure

```
pneumonia-detection/
├── app.py                          # Flask backend server
├── index.html                      # React frontend (single file)
├── requirements.txt                # Python dependencies
├── viral_pneumonia_model.pth       # Your trained model
└── README.md                       # This file
```

## 🚀 Future Enhancements

- [ ] Add batch processing progress bar
- [ ] Export results to PDF report
- [ ] Compare multiple X-rays side-by-side
- [ ] Add image preprocessing options
- [ ] Support for DICOM format
- [ ] Multi-class predictions (COVID, bacterial pneumonia, etc.)
- [ ] Historical results tracking
- [ ] Model explanation/visualization (Grad-CAM)

## 📄 License

This project is for educational purposes. Ensure you have the right to use the training data and comply with medical AI regulations in your jurisdiction.

## 🤝 Contributing

This is a template project. Feel free to:
- Improve the UI/UX
- Add new features
- Optimize model performance
- Enhance error handling

## 📧 Support

If you encounter issues:
1. Check the troubleshooting section
2. Verify all dependencies are installed
3. Ensure the model file is in the correct location
4. Check browser console for errors (F12)

## 🎓 Credits

- Model training dataset: COVID-19 Radiography Database
- Framework: PyTorch, Flask, React
- Model architecture: ResNet18

---

**Remember**: This tool is for research and education only. Never use it as a substitute for professional medical diagnosis! 🏥

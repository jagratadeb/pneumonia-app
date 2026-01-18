# 🚀 Quick Start Guide - Pneumonia Detection AI

## What You Got

A complete pneumonia detection web application with:
- **Backend**: Python Flask server with PyTorch
- **Frontend**: Beautiful React web interface
- **Model**: Ready to use your trained ResNet18 model

## Files Included

```
📦 Your Project
├── 📄 app.py                      # Backend server
├── 📄 index.html                  # Web interface
├── 📄 requirements.txt            # Python packages
├── 📄 test_setup.py              # Setup verification
├── 📄 README.md                   # Full documentation
└── 📄 QUICK_START.md             # This file
```

## ⚡ 3-Minute Setup

### Step 1: Install Dependencies (1 min)
```bash
pip install flask flask-cors torch torchvision Pillow
```

### Step 2: Add Your Model (30 sec)
Place `viral_pneumonia_model.pth` in the same folder as `app.py`

### Step 3: Start Backend (30 sec)
```bash
python app.py
```

### Step 4: Open Frontend (30 sec)
Double-click `index.html` or drag it to your browser

## ✅ Verify Setup
```bash
python test_setup.py
```

## 🎯 How to Use

1. **Upload**: Drag X-ray images to the upload area
2. **Analyze**: Click "Analyze" button
3. **Results**: View predictions with confidence scores

## 🎨 Features

- 📤 Multiple image upload
- 🖱️ Drag and drop support
- 📊 Confidence scores
- 🎨 Color-coded results
- 📱 Mobile responsive

## ⚠️ Requirements

- Python 3.8+
- Your `viral_pneumonia_model.pth` file
- Modern web browser

## 🐛 Common Issues

| Problem | Solution |
|---------|----------|
| Backend won't start | Run: `pip install -r requirements.txt` |
| Can't find model | Place `.pth` file with `app.py` |
| CORS errors | Make sure backend is running first |
| Predictions fail | Check browser console (F12) for errors |

## 📞 Need Help?

1. Read the full **README.md** for detailed docs
2. Run `python test_setup.py` to diagnose issues
3. Check backend terminal for error messages

## 🎓 Model Details

- **Type**: Binary Classification
- **Architecture**: ResNet18
- **Input**: 224x224 RGB images
- **Classes**:
  - 🟢 Normal/Other (Class 0)
  - 🔴 Viral Pneumonia (Class 1)

## 🚨 Important

This is for **research/education only**. Not for medical diagnosis!
Always consult healthcare professionals.

## 🎉 You're Ready!

```bash
# Terminal 1: Start backend
python app.py

# Terminal 2: Test it
python test_setup.py

# Browser: Open index.html
```

Happy analyzing! 🔬

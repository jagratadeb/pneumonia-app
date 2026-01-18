import os
import requests
import sys

def test_setup():
    print("=" * 60)
    print("Pneumonia Detection Setup Verification")
    print("=" * 60)
    
    # Check if model file exists
    print("\n1. Checking for model file...")
    if os.path.exists('viral_pneumonia_model.pth'):
        print("   ✓ viral_pneumonia_model.pth found")
    else:
        print("   ✗ viral_pneumonia_model.pth NOT FOUND")
        print("   → Please place your .pth file in this directory")
        return False
    
    # Check if required files exist
    print("\n2. Checking for required files...")
    required_files = ['app.py', 'index.html', 'requirements.txt']
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"   ✓ {file} found")
        else:
            print(f"   ✗ {file} NOT FOUND")
            all_exist = False
    
    if not all_exist:
        return False
    
    # Check if backend is running
    print("\n3. Checking if backend server is running...")
    try:
        response = requests.get('http://localhost:5000/health', timeout=5)
        if response.status_code == 200:
            data = response.json()
            print("   ✓ Backend server is running")
            print(f"   ✓ Model loaded: {data.get('model_loaded', False)}")
        else:
            print("   ✗ Backend server responded with error")
            return False
    except requests.exceptions.ConnectionError:
        print("   ✗ Backend server is NOT running")
        print("   → Please start the server with: python app.py")
        return False
    except Exception as e:
        print(f"   ✗ Error connecting to backend: {e}")
        return False
    
    # Check Python dependencies
    print("\n4. Checking Python dependencies...")
    dependencies = ['flask', 'flask_cors', 'torch', 'torchvision', 'PIL']
    all_installed = True
    for dep in dependencies:
        try:
            __import__(dep)
            print(f"   ✓ {dep} installed")
        except ImportError:
            print(f"   ✗ {dep} NOT INSTALLED")
            all_installed = False
    
    if not all_installed:
        print("\n   → Install missing dependencies with:")
        print("   pip install -r requirements.txt")
        return False
    
    print("\n" + "=" * 60)
    print("✓ Setup verification PASSED!")
    print("=" * 60)
    print("\nYou're ready to use the pneumonia detection app!")
    print("\nNext steps:")
    print("1. Make sure backend is running: python app.py")
    print("2. Open index.html in your web browser")
    print("3. Upload X-ray images and start analyzing!")
    print("\n" + "=" * 60)
    return True

if __name__ == '__main__':
    success = test_setup()
    sys.exit(0 if success else 1)

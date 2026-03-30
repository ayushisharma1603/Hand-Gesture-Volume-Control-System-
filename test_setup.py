"""
Test script to verify all dependencies and components are working correctly.
Run this before running main.py to ensure everything is set up properly.
"""

import sys
import subprocess

def test_imports():
    """Test if all required packages can be imported."""
    print("=" * 50)
    print("Testing Imports...")
    print("=" * 50)
    
    packages = {
        'cv2': 'OpenCV',
        'mediapipe': 'MediaPipe',
        'numpy': 'NumPy',
        'pycaw': 'pycaw',
        'comtypes': 'comtypes'
    }
    
    all_ok = True
    for package, name in packages.items():
        try:
            __import__(package)
            print(f"✓ {name}: OK")
        except ImportError as e:
            print(f"✗ {name}: FAILED - {e}")
            all_ok = False
    
    return all_ok

def test_camera():
    """Test if camera is accessible."""
    print("\n" + "=" * 50)
    print("Testing Camera...")
    print("=" * 50)
    
    try:
        import cv2
        cap = cv2.VideoCapture(0)
        
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                print(f"✓ Camera: OK (Resolution: {frame.shape[1]}x{frame.shape[0]})")
                cap.release()
                return True
            else:
                print("✗ Camera: Failed to capture frame")
                cap.release()
                return False
        else:
            print("✗ Camera: Not accessible")
            return False
    except Exception as e:
        print(f"✗ Camera: Error - {e}")
        return False

def test_hand_detection():
    """Test hand detection capability."""
    print("\n" + "=" * 50)
    print("Testing Hand Detection...")
    print("=" * 50)
    
    try:
        from hand_detector import HandDetector
        detector = HandDetector()
        print("✓ Hand Detector: Initialized successfully")
        return True
    except Exception as e:
        print(f"✗ Hand Detector: Failed - {e}")
        return False

def test_gesture_recognition():
    """Test gesture recognition capability."""
    print("\n" + "=" * 50)
    print("Testing Gesture Recognition...")
    print("=" * 50)
    
    try:
        from gesture_recognition import GestureRecognizer
        recognizer = GestureRecognizer()
        print("✓ Gesture Recognizer: Initialized successfully")
        return True
    except Exception as e:
        print(f"✗ Gesture Recognizer: Failed - {e}")
        return False

def test_volume_control():
    """Test volume control capability."""
    print("\n" + "=" * 50)
    print("Testing Volume Control...")
    print("=" * 50)
    
    try:
        from volume_controller import VolumeController
        controller = VolumeController()
        
        if controller.volume is None:
            print("⚠ Volume Control: Initialized but audio device not accessible")
            print("  Note: Run with administrator privileges for volume control")
            return False
        
        current_volume = controller.get_volume()
        print(f"✓ Volume Control: OK (Current volume: {current_volume:.1f}%)")
        return True
    except Exception as e:
        print(f"⚠ Volume Control: Warning - {e}")
        print("  Run with administrator privileges for full functionality")
        return False

def install_requirements():
    """Install missing requirements."""
    print("\n" + "=" * 50)
    print("Installing Requirements...")
    print("=" * 50)
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Requirements installed successfully")
        return True
    except Exception as e:
        print(f"✗ Failed to install requirements: {e}")
        return False

def main():
    """Run all tests."""
    print("\n")
    print("╔" + "=" * 48 + "╗")
    print("║" + " Hand Gesture Volume Control - Setup Test ".center(48) + "║")
    print("╚" + "=" * 48 + "╝")
    print()
    
    # Test imports
    if not test_imports():
        print("\n⚠ Some packages are missing. Installing requirements...\n")
        if not install_requirements():
            print("\n✗ Failed to install requirements. Please run:")
            print("  pip install -r requirements.txt")
            sys.exit(1)
        print("\nRetesting imports...")
        if not test_imports():
            print("\n✗ Setup failed. Please check your Python installation.")
            sys.exit(1)
    
    # Test camera
    camera_ok = test_camera()
    
    # Test components
    detector_ok = test_hand_detection()
    gesture_ok = test_gesture_recognition()
    volume_ok = test_volume_control()
    
    # Summary
    print("\n" + "=" * 50)
    print("Test Summary")
    print("=" * 50)
    
    all_critical_ok = camera_ok and detector_ok and gesture_ok
    
    if all_critical_ok:
        print("\n✓ All critical components are working!")
        if volume_ok:
            print("✓ Volume control is ready!")
            print("\nYou can now run: python main.py")
        else:
            print("⚠ Volume control may not work. Run with administrator privileges:")
            print("  Right-click Command Prompt → Run as administrator")
            print("  Then run: python main.py")
    else:
        print("\n✗ Some critical components failed.")
        print("Please check the errors above and try again.")
        sys.exit(1)

if __name__ == "__main__":
    main()

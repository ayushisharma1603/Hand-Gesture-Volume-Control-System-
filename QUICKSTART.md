# Quick Start Guide - Hand Gesture Volume Control System

## Step 1: Install Dependencies (First Time Only)

Open PowerShell in the project directory and run:

```powershell
pip install -r requirements.txt
```

This will install all required packages:
- OpenCV (computer vision)
- MediaPipe (hand detection)
- NumPy (numerical computing)
- pycaw (Windows volume control)

## Step 2: Test Everything

Before running the main application, verify all components are working:

```powershell
python test_setup.py
```

This will check:
- ✓ All Python packages installed correctly
- ✓ Camera is accessible
- ✓ Hand detection module works
- ✓ Gesture recognition is ready
- ✓ Volume control is accessible

## Step 3: Run the Application

```powershell
python main.py
```

## Gesture Cheat Sheet

| Gesture | Action |
|---------|--------|
| 👍 Thumbs Up | Volume Up |
| 👎 Thumbs Down | Volume Down |
| ✌️ Peace Sign | Mute / Unmute |
| 👌 OK Sign | Play / Pause |
| 🤘 Rock Sign | Next Track |
| ✊ Fist | Previous Track |
| ✋ Open Palm | Stop |

## Tips for Success

1. **Lighting**: Ensure good, even lighting
2. **Distance**: Position yourself 1-3 feet from camera
3. **Clarity**: Make clear, deliberate gestures
4. **Patience**: Give the system a moment between gestures (≈0.3 seconds)

## Troubleshooting Quick Links

- **Camera not working?** 
  - Close other apps using your camera
  - Check Windows Settings → Privacy → Camera
  
- **Volume control not working?**
  - Run PowerShell as Administrator
  - Restart the application
  
- **Gestures not recognized?**
  - Improve lighting
  - Make bigger gestures
  - Check that your entire hand is visible

## File Guide

| File | Purpose |
|------|---------|
| `main.py` | Run this to start |
| `test_setup.py` | Run this to verify setup |
| `config.py` | Customize settings here |
| `README.md` | Full documentation |
| `requirements.txt` | Python dependencies |

## Next Steps

1. ✓ Run `test_setup.py` to verify everything works
2. ✓ Run `main.py` to start using the system
3. ✓ Open `config.py` to customize settings if desired
4. ✓ Refer to `README.md` for advanced configuration

---

**Stuck?** Check the README.md file for detailed troubleshooting!

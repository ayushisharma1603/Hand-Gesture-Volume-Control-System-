# Hand Gesture Volume Control System

A Python-based computer vision application that recognizes hand gestures to control Windows system volume and media playback.

## Features

- ✋ Real-time hand detection and landmark tracking
- 🤘 Multiple gesture recognition:
  - **Thumbs Up**: Increase volume
  - **Thumbs Down**: Decrease volume  
  - **Peace Sign** (2 fingers): Mute/Unmute
  - **OK Sign**: Play/Pause
  - **Rock Sign**: Next track
  - **Fist**: Previous track
  - **Open Palm**: Stop
- 🔊 Direct Windows system volume control
- 📊 Real-time FPS and status display
- 🎯 Gesture smoothing to reduce false positives

## Requirements

- Python 3.7 or higher
- Windows OS (10 or later recommended)
- Webcam/Camera
- 4GB RAM minimum

## Installation

### 1. Clone or Download Project

```bash
cd c:\Users\hp\Desktop\hand
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
```

Activate it:
- **Windows (PowerShell)**:
  ```bash
  .\venv\Scripts\Activate.ps1
  ```
- **Windows (CMD)**:
  ```bash
  venv\Scripts\activate.bat
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- **opencv-python**: Computer vision library
- **mediapipe**: Hand detection and pose estimation
- **numpy**: Numerical computing
- **pycaw**: Windows audio control
- **comtypes**: Windows COM library

## Quick Start

### Run the Application

```bash
python main.py
```

### Controls

Once the application is running:
- **Thumbs Up**: Move thumb upward → Volume Up
- **Thumbs Down**: Move thumb downward → Volume Down
- **Peace Sign**: Extend index and middle fingers → Mute/Unmute
- **OK Sign**: Touch index to thumb, other fingers extended → Play/Pause
- **Rock Sign**: Extend index and pinky → Next Track
- **Fist**: Close all fingers → Previous Track
- **Open Palm**: Open all fingers → Stop

Press **'Q'** to quit the application.

## Project Structure

```
hand/
├── main.py                      # Main application entry point
├── hand_detector.py             # Hand detection using MediaPipe
├── gesture_recognition.py       # Gesture recognition logic
├── volume_controller.py         # Windows volume control
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## File Descriptions

### main.py
- Orchestrates the entire application
- Captures video from webcam
- Manages the main loop
- Draws UI elements (info panel, volume bar)
- Handles user input

### hand_detector.py
- Uses MediaPipe for hand detection
- Extracts hand landmarks (21 points per hand)
- Calculates distances between landmarks
- Renders hand visualization

### gesture_recognition.py
- Implements gesture detection algorithms
- Recognizes specific hand poses
- Stabilizes gestures to reduce jitter
- Maintains gesture history

### volume_controller.py
- Controls Windows system volume via pycaw
- Implements cooldown mechanism for gestures
- Tracks volume level
- Translates gestures to volume actions

### requirements.txt
- Lists all Python package dependencies
- Specifies compatible versions

## Troubleshooting

### Issue: Camera not detected

**Solution**: Check that your webcam is connected and not in use by another application.

```bash
# Test if OpenCV can find your camera:
python -c "import cv2; cap = cv2.VideoCapture(0); print('Camera OK' if cap.isOpened() else 'Camera Failed')"
```

### Issue: Volume control not working

**Solution**: 
1. Ensure pycaw is properly installed:
   ```bash
   pip install --upgrade pycaw
   ```
2. Run the application with administrator privileges
3. Check Windows audio settings

### Issue: Gestures not being recognized

**Troubleshooting**:
1. Ensure adequate lighting
2. Keep hands within frame
3. Make clear, distinct gestures
4. Check console output for error messages

### Issue: High CPU usage

**Solution**:
1. Reduce camera resolution in `main.py`
2. Lower the FPS limit
3. Use a faster computer for real-time processing

## Advanced Configuration

### Adjust Volume Change Amount

In `volume_controller.py`, modify the `amount` parameter:

```python
def increase_volume(self, amount: float = 5):  # Change 5 to desired increment
```

### Change Gesture Cooldown

In `volume_controller.py`, modify:

```python
self.gesture_cooldown = 0.3  # Change to desired cooldown in seconds
```

### Adjust Detection Confidence

In `hand_detector.py`, modify:

```python
self.hands = self.mp_hands.Hands(
    detection_confidence=0.7  # Range: 0.0 to 1.0
)
```

## Performance Tips

1. **Good Lighting**: Ensure well-lit environment for best hand detection
2. **Camera Position**: Position camera at eye level, 2-3 feet away
3. **Hand Visibility**: Keep hands fully visible in frame
4. **Clean Environment**: Clutter-free background helps detection
5. **Sufficient Space**: Have adequate space to make gestures

## Limitations

- Works best with single hand gestures (though it supports up to 2 hands)
- Requires clear visibility of hands
- Gesture recognition depends on lighting conditions
- Works only on Windows (due to pycaw)

## Future Enhancements

- [ ] Support for Linux and macOS (alternative audio libraries)
- [ ] Machine learning-based gesture customization
- [ ] Multi-hand simultaneous gesture support
- [ ] Gesture recording and playback
- [ ] Application-specific volume control (Spotify, YouTube, etc.)
- [ ] Hand tracking confidence visualization
- [ ] Custom gesture definition UI

## Technical Details

### MediaPipe Hand Landmarks

The system tracks 21 hand landmarks:
- 0: Wrist
- 1-4: Thumb
- 5-8: Index Finger
- 9-12: Middle Finger
- 13-16: Ring Finger
- 17-20: Pinky Finger

### Gesture Detection Algorithm

Gestures are detected using:
1. **Landmark Position Analysis**: Comparing relative positions of hand joints
2. **Distance Calculations**: Euclidean distance between specific points
3. **Temporal Smoothing**: Requiring gesture stability over multiple frames
4. **Cooldown Mechanism**: Preventing rapid repeated triggers

## License

This project is provided as-is for educational purposes.

## Support

For issues or questions:
1. Check the Troubleshooting section
2. Review the console output for error messages
3. Verify all dependencies are correctly installed
4. Ensure adequate lighting and camera setup

## Author

Created for Computer Vision Project

## References

- [MediaPipe Documentation](https://mediapipe.dev/)
- [OpenCV Documentation](https://opencv.org/)
- [pycaw GitHub](https://github.com/AndreMiras/pycaw)

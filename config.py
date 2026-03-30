# Configuration file for Hand Gesture Volume Control System

# Camera settings
CAMERA_INDEX = 0  # 0 for default camera, 1, 2... for other cameras
FRAME_WIDTH = 1280
FRAME_HEIGHT = 720
FPS_LIMIT = 30

# Hand detection settings
MAX_HANDS = 2
DETECTION_CONFIDENCE = 0.7
TRACKING_CONFIDENCE = 0.5

# Gesture recognition settings
GESTURE_HISTORY_SIZE = 5  # Number of frames to smooth gestures
GESTURE_COOLDOWN = 0.3    # Seconds between gesture actions

# Volume control settings
VOLUME_INCREMENT = 5      # Percentage to change volume per gesture
VOLUME_DECREMENT = 5      # Percentage to change volume per gesture

# Display settings
SHOW_FPS = True
SHOW_GESTURE_INFO = True
SHOW_VOLUME_BAR = True
SHOW_LANDMARKS = True

# Debug settings
DEBUG_MODE = False
VERBOSE = False

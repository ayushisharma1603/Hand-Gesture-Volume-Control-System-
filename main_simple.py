import cv2
import mediapipe as mp
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

print("🚀 Starting Hand Gesture Volume Control System...")

# Initialize MediaPipe
print("📱 Initializing MediaPipe...")
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# Initialize Volume Control
print("🔊 Initializing Volume Control...")
try:
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    minVol, maxVol = volume.GetVolumeRange()[:2]
    print("✅ Volume control initialized successfully")
except Exception as e:
    print(f"❌ Warning: Volume control not available: {e}")
    volume = None
    minVol, maxVol = 0, 0

# Start webcam
print("📹 Opening camera...")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Cannot open camera")
    exit(1)

print("✅ Camera opened successfully")
print("\n" + "="*50)
print("HAND GESTURE VOLUME CONTROL")
print("="*50)
print("\n📍 GESTURES:")
print("  👍 Thumbs Up/Down: Increase/Decrease Volume")
print("  ✌️  Index & Thumb Close: Control Volume by Distance")
print("\n⌨️  Press 'Q' to quit\n")
print("="*50 + "\n")

frame_count = 0
fps_time = 0

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("❌ Error: Failed to capture frame")
        break
    
    # Flip frame for mirror view
    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape
    
    # Convert to RGB
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    
    # Process hand landmarks
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # Draw hand skeleton
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
            
            thumb = None
            index = None
            
            # Get thumb (id=4) and index (id=8) positions
            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                
                if id == 4:
                    thumb = (cx, cy)
                if id == 8:
                    index = (cx, cy)
            
            # Calculate distance and control volume
            if thumb and index:
                # Draw circles and line
                cv2.circle(frame, thumb, 10, (255, 0, 0), -1)
                cv2.circle(frame, index, 10, (255, 0, 0), -1)
                cv2.line(frame, thumb, index, (255, 0, 0), 3)
                
                # Calculate distance
                length = np.hypot(index[0] - thumb[0], index[1] - thumb[1])
                
                # Map distance to volume (20-200 pixels to min-max volume)
                if volume is not None:
                    vol = np.interp(length, [20, 200], [minVol, maxVol])
                    volume.SetMasterVolumeLevel(vol, None)
                
                # Calculate volume percentage
                vol_percent = int(np.interp(length, [20, 200], [0, 100]))
                
                # Display volume info
                cv2.putText(frame, f'Volume: {vol_percent}%', (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                cv2.putText(frame, f'Distance: {int(length)} px', (50, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
    
    # Display FPS
    frame_count += 1
    if frame_count % 10 == 0:
        fps_time = frame_count
    
    cv2.putText(frame, "Press 'Q' to quit", (w - 300, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    
    # Show frame
    cv2.imshow("Hand Gesture Volume Control", frame)
    
    # Wait for key press
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == ord('Q'):
        print("\n✅ Closing application...")
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
print("✅ Application closed successfully!")

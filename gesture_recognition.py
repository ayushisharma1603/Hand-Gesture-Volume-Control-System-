import numpy as np
from typing import Tuple, Optional
from hand_detector import HandDetector

class GestureRecognizer:
    """
    Recognizes hand gestures for volume control.
    """
    
    def __init__(self):
        """Initialize gesture recognizer."""
        self.hand_detector = HandDetector()
        self.gesture_history = []
        self.history_size = 5  # Smooth gestures over 5 frames
        
    def is_finger_up(self, landmarks, finger_tip_idx: int, finger_pip_idx: int) -> bool:
        """
        Check if a finger is extended (up).
        
        Args:
            landmarks: List of hand landmarks
            finger_tip_idx: Index of finger tip landmark
            finger_pip_idx: Index of finger PIP landmark
        """
        return landmarks[finger_tip_idx][1] < landmarks[finger_pip_idx][1]
    
    def count_fingers_up(self, landmarks) -> int:
        """
        Count how many fingers are extended.
        
        Returns:
            Number of fingers up (0-5)
        """
        fingers_up = 0
        
        # Thumb (special case - check horizontal)
        if landmarks[4][0] < landmarks[3][0]:  # Right hand
            fingers_up += 1
        
        # Other four fingers
        finger_tips = [8, 12, 16, 20]
        finger_pips = [6, 10, 14, 18]
        
        for tip, pip in zip(finger_tips, finger_pips):
            if self.is_finger_up(landmarks, tip, pip):
                fingers_up += 1
        
        return fingers_up
    
    def detect_thumbs_up(self, landmarks) -> bool:
        """Detect thumbs up gesture."""
        # Thumb tip should be above thumb PIP
        # Index, middle, ring, pinky should be closed
        
        # Check if thumb is up
        thumb_up = landmarks[4][1] < landmarks[3][1]
        
        # Check if other fingers are closed
        other_fingers_closed = True
        for tip, pip in [(8, 6), (12, 10), (16, 14), (20, 18)]:
            if self.is_finger_up(landmarks, tip, pip):
                other_fingers_closed = False
                break
        
        return thumb_up and other_fingers_closed
    
    def detect_thumbs_down(self, landmarks) -> bool:
        """Detect thumbs down gesture."""
        # Thumb tip should be below thumb PIP
        # Index, middle, ring, pinky should be closed
        
        # Check if thumb is down
        thumb_down = landmarks[4][1] > landmarks[3][1]
        
        # Check if other fingers are closed
        other_fingers_closed = True
        for tip, pip in [(8, 6), (12, 10), (16, 14), (20, 18)]:
            if self.is_finger_up(landmarks, tip, pip):
                other_fingers_closed = False
                break
        
        return thumb_down and other_fingers_closed
    
    def detect_peace_sign(self, landmarks) -> bool:
        """
        Detect peace sign (two fingers extended).
        Used for mute toggle.
        """
        fingers_up = self.count_fingers_up(landmarks)
        return fingers_up == 2
    
    def detect_ok_sign(self, landmarks) -> bool:
        """
        Detect OK sign (index and thumb close, other fingers up).
        Used for play/pause.
        """
        # Index and thumb should be close
        index_thumb_distance = self.hand_detector.distance(
            landmarks[4], landmarks[8]
        )
        
        fingers_up = 0
        for tip, pip in [(12, 10), (16, 14), (20, 18)]:
            if self.is_finger_up(landmarks, tip, pip):
                fingers_up += 1
        
        return index_thumb_distance < 30 and fingers_up == 3
    
    def detect_rock_sign(self, landmarks) -> bool:
        """
        Detect rock sign (index and pinky up, others down).
        Used for next track.
        """
        # Index and pinky should be up
        index_up = self.is_finger_up(landmarks, 8, 6)
        pinky_up = self.is_finger_up(landmarks, 20, 18)
        
        # Middle and ring should be down
        middle_down = not self.is_finger_up(landmarks, 12, 10)
        ring_down = not self.is_finger_up(landmarks, 16, 14)
        
        return index_up and pinky_up and middle_down and ring_down
    
    def detect_fist(self, landmarks) -> bool:
        """
        Detect closed fist (all fingers closed).
        Used for previous track.
        """
        fingers_up = self.count_fingers_up(landmarks)
        return fingers_up == 0
    
    def detect_open_palm(self, landmarks) -> bool:
        """
        Detect open palm (all fingers extended).
        Used for stop.
        """
        fingers_up = self.count_fingers_up(landmarks)
        return fingers_up >= 5
    
    def recognize_gesture(self, landmarks) -> str:
        """
        Recognize the gesture from hand landmarks.
        
        Returns:
            Gesture name or 'none'
        """
        # Check gestures in order of specificity
        if self.detect_thumbs_up(landmarks):
            return 'thumbs_up'
        elif self.detect_thumbs_down(landmarks):
            return 'thumbs_down'
        elif self.detect_peace_sign(landmarks):
            return 'peace_sign'
        elif self.detect_ok_sign(landmarks):
            return 'ok_sign'
        elif self.detect_rock_sign(landmarks):
            return 'rock_sign'
        elif self.detect_fist(landmarks):
            return 'fist'
        elif self.detect_open_palm(landmarks):
            return 'open_palm'
        else:
            return 'none'
    
    def get_stable_gesture(self, gesture: str) -> Optional[str]:
        """
        Return gesture only if stable over multiple frames.
        This reduces jitter and false positives.
        """
        self.gesture_history.append(gesture)
        
        if len(self.gesture_history) > self.history_size:
            self.gesture_history.pop(0)
        
        # If most recent frames show same gesture, return it
        if len(self.gesture_history) >= self.history_size:
            if (self.gesture_history.count(gesture) >= self.history_size - 1 and 
                gesture != 'none'):
                return gesture
        
        return None

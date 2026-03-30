import cv2
import numpy as np
from typing import List, Tuple, Optional
import mediapipe as mp

class HandDetector:
    """
    Detects and tracks hands in video frames using MediaPipe.
    """
    
    def __init__(self, mode=False, max_hands=2, detection_confidence=0.7, tracking_confidence=0.5):
        """
        Initialize the hand detector.
        
        Args:
            mode: Static image mode (False for video)
            max_hands: Maximum number of hands to detect
            detection_confidence: Minimum confidence for detection
            tracking_confidence: Minimum confidence for tracking
        """
        self.mode = mode
        self.max_hands = max_hands
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence
        
        # Initialize MediaPipe Hands
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        
        self.hands = self.mp_hands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.max_hands,
            min_detection_confidence=self.detection_confidence,
            min_tracking_confidence=self.tracking_confidence
        )
        
    def find_hands(self, frame: np.ndarray, draw=True) -> Tuple[np.ndarray, List]:
        """
        Detect hands in a frame.
        
        Args:
            frame: Input frame
            draw: Whether to draw landmarks on frame
            
        Returns:
            Tuple of (processed frame, list of hand landmarks)
        """
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        
        hands_list = []
        frame_height, frame_width, _ = frame.shape
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                if draw:
                    self.mp_drawing.draw_landmarks(
                        frame,
                        hand_landmarks,
                        self.mp_hands.HAND_CONNECTIONS
                    )
                
                # Extract landmark coordinates
                landmarks = []
                for lm in hand_landmarks.landmark:
                    x = int(lm.x * frame_width)
                    y = int(lm.y * frame_height)
                    landmarks.append((x, y))
                
                hands_list.append(landmarks)
        
        return frame, hands_list
    
    def get_landmark_positions(self, landmarks: List[Tuple[int, int]]) -> dict:
        """
        Get specific landmark positions from a hand.
        
        MediaPipe landmarks:
        0: Wrist, 4: Thumb tip, 8: Index tip, 12: Middle tip, 
        16: Ring tip, 20: Pinky tip
        """
        return {
            'wrist': landmarks[0],
            'thumb_tip': landmarks[4],
            'index_tip': landmarks[8],
            'middle_tip': landmarks[12],
            'ring_tip': landmarks[16],
            'pinky_tip': landmarks[20],
            'index_pip': landmarks[6],
            'middle_pip': landmarks[10],
            'ring_pip': landmarks[14],
            'pinky_pip': landmarks[18],
        }
    
    def distance(self, p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
        """Calculate Euclidean distance between two points."""
        return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
import time

class VolumeController:
    """
    Controls Windows system volume and media playback.
    """
    
    def __init__(self):
        """Initialize volume controller."""
        self.last_gesture_time = {}  # Track last time each gesture was executed
        self.gesture_cooldown = 0.3  # Seconds between gesture actions
        self.current_volume = self.get_volume()
        
        try:
            # Get the default audio device
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(
                IAudioEndpointVolume._iid_, cast(None, POINTER(None)), None
            )
            self.volume = cast(interface, POINTER(IAudioEndpointVolume))
            self.volume_range = self.volume.GetVolumeRange()
        except Exception as e:
            print(f"Warning: Could not initialize volume controller: {e}")
            self.volume = None
            self.volume_range = (0, 0)
    
    def get_volume(self) -> float:
        """
        Get current volume level (0-100).
        """
        if self.volume is None:
            return 0
        
        try:
            current_volume_db = self.volume.GetMasterVolumeLevel()
            min_vol, max_vol, _ = self.volume_range
            
            # Convert dB to percentage
            if max_vol - min_vol == 0:
                return 0
            
            current_volume_percent = ((current_volume_db - min_vol) / (max_vol - min_vol)) * 100
            return max(0, min(100, current_volume_percent))
        except Exception as e:
            print(f"Error getting volume: {e}")
            return 0
    
    def set_volume(self, volume_percent: float):
        """
        Set volume level (0-100).
        
        Args:
            volume_percent: Volume level from 0 to 100
        """
        if self.volume is None:
            return
        
        try:
            volume_percent = max(0, min(100, volume_percent))
            min_vol, max_vol, _ = self.volume_range
            
            # Convert percentage to dB
            volume_db = min_vol + (volume_percent / 100) * (max_vol - min_vol)
            self.volume.SetMasterVolumeLevel(volume_db, None)
            self.current_volume = volume_percent
        except Exception as e:
            print(f"Error setting volume: {e}")
    
    def increase_volume(self, amount: float = 5):
        """Increase volume by percentage."""
        new_volume = min(100, self.get_volume() + amount)
        self.set_volume(new_volume)
        print(f"Volume: {new_volume:.1f}%")
    
    def decrease_volume(self, amount: float = 5):
        """Decrease volume by percentage."""
        new_volume = max(0, self.get_volume() - amount)
        self.set_volume(new_volume)
        print(f"Volume: {new_volume:.1f}%")
    
    def toggle_mute(self):
        """Toggle mute on/off."""
        if self.volume is None:
            return
        
        try:
            is_muted = self.volume.GetMute()
            self.volume.SetMute(not is_muted, None)
            print(f"Mute: {'ON' if not is_muted else 'OFF'}")
        except Exception as e:
            print(f"Error toggling mute: {e}")
    
    def play_pause(self):
        """Simulate play/pause media key."""
        try:
            import pyaudio
            # This is a placeholder - in production, you'd use Windows API
            # or keyboard simulation
            print("Play/Pause triggered")
        except Exception as e:
            print(f"Error: {e}")
    
    def next_track(self):
        """Simulate next track media key."""
        print("Next track triggered")
    
    def previous_track(self):
        """Simulate previous track media key."""
        print("Previous track triggered")
    
    def can_execute_gesture(self, gesture_name: str) -> bool:
        """
        Check if enough time has passed since last execution of this gesture.
        Prevents rapid repeated triggers.
        """
        current_time = time.time()
        last_time = self.last_gesture_time.get(gesture_name, 0)
        
        if current_time - last_time >= self.gesture_cooldown:
            self.last_gesture_time[gesture_name] = current_time
            return True
        
        return False
    
    def execute_gesture(self, gesture: str):
        """
        Execute action for recognized gesture.
        
        Args:
            gesture: Gesture name
        """
        if not self.can_execute_gesture(gesture):
            return
        
        gesture_actions = {
            'thumbs_up': self.increase_volume,
            'thumbs_down': self.decrease_volume,
            'peace_sign': self.toggle_mute,
            'ok_sign': self.play_pause,
            'rock_sign': self.next_track,
            'fist': self.previous_track,
            'open_palm': lambda: print("Gesture: Open palm detected")
        }
        
        action = gesture_actions.get(gesture)
        if action:
            action()

# 🖐️ Touchless Volume Control System using Hand Gesture Recognition

> 🚀 **AI-powered Computer Vision Project for Smart Human-Computer Interaction**

---

## 📌 Overview

This project is a **real-time hand gesture recognition system** that allows users to control system volume and media playback without physical interaction.

Using **Computer Vision and AI**, the system detects hand gestures through a webcam and translates them into system commands.

👉 Designed as a **practical application of AI in Human-Computer Interaction (HCI)**.

---

## 🎯 Problem Statement

Traditional system controls (keyboard/mouse) are:

* ❌ Not intuitive
* ❌ Not touchless
* ❌ Limited for accessibility

👉 This project introduces a **gesture-based touchless interface** for a more natural and interactive experience.

---

## 💡 Key Features

✨ Real-time hand detection using webcam
✨ Accurate gesture recognition using AI
✨ Touchless volume control
✨ Media playback control (Play/Pause/Next/Previous)
✨ Smooth gesture handling to avoid false triggers
✨ Live FPS and system feedback display

---

## 🧠 Tech Stack

| Technology | Purpose                            |
| ---------- | ---------------------------------- |
| Python     | Core programming                   |
| OpenCV     | Image processing                   |
| MediaPipe  | Hand tracking & landmark detection |
| NumPy      | Mathematical computations          |
| Pycaw      | Windows volume control             |

---

## ⚙️ How It Works

1️⃣ Webcam captures live video
2️⃣ MediaPipe detects **21 hand landmarks**
3️⃣ Gesture recognition algorithm analyzes finger positions
4️⃣ System maps gestures → actions
5️⃣ Volume/media is controlled in real-time

---

## ✋ Supported Gestures

| Gesture        | Action          |
| -------------- | --------------- |
| 👍 Thumbs Up   | Increase Volume |
| 👎 Thumbs Down | Decrease Volume |
| ✌️ Peace Sign  | Mute / Unmute   |
| 👌 OK Sign     | Play / Pause    |
| 🤘 Rock Sign   | Next Track      |
| ✊ Fist         | Previous Track  |
| 🖐 Open Palm   | Stop            |

---

## ▶️ How to Run

### Step 1: Install Dependencies

```bash
pip install mediapipe==0.10.9 numpy==1.24.3 opencv-python pycaw comtypes
```

### Step 2: Run Application

```bash
python main.py
```

---

## 📊 Output

* Live webcam feed
* Hand tracking visualization
* Gesture detection in real-time
* Dynamic volume/media control

---

## 📁 Project Structure

```
hand-gesture-control/
│
├── main.py
├── hand_detector.py
├── gesture_recognition.py
├── volume_controller.py
├── requirements.txt
└── README.md
```

---

## 🧪 Performance Highlights

* ⚡ Real-time processing (30+ FPS)
* 🎯 Accurate gesture detection
* 🔄 Smooth interaction with reduced jitter
* 🧠 Efficient landmark-based detection (no heavy model training required)

---

## ⚠️ Limitations

* Works best in good lighting conditions
* Requires clear hand visibility
* Windows only (due to Pycaw dependency)

---

## 🚀 Future Enhancements

* 🔹 Cross-platform support (Linux/macOS)
* 🔹 Custom gesture training using ML
* 🔹 Multi-hand gesture support
* 🔹 Integration with apps (Spotify, YouTube)
* 🔹 Gesture-based UI dashboard

---

## 🧠 Learning Outcomes

✔ Practical implementation of Computer Vision
✔ Real-time hand tracking using MediaPipe
✔ Gesture recognition logic development
✔ System-level integration (volume/media control)
✔ Understanding of Human-Computer Interaction systems

---

## 👩‍💻 Author

**Ayushi Sharma**
B.Tech CSE (AI) | VIT Bhopal

---

## ⭐ Why This Project Matters (For Placements)

This project demonstrates:

✅ Real-world problem solving using AI
✅ Strong understanding of Computer Vision
✅ Ability to build real-time systems
✅ Integration of software with hardware (webcam + OS control)

👉 Makes your profile stand out in:

* AI/ML roles
* Software Developer roles
* Product-based companies

---

## 📢 Conclusion

This project showcases how **AI can transform traditional interfaces into intuitive, touchless systems**, paving the way for smarter and more accessible technology.

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it! 🚀


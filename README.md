# GestureVision AI – Real-Time Hand Gesture Recognition System
## 🧠 Overview
GestureVision AI is a real-time hand gesture recognition system that uses computer vision and machine learning techniques to detect and classify hand gestures from live video streams.

🎯 Features
-🔍 Real-time hand detection
-✋ Gesture classification
-🎥 Works with webcam/live feed
-⚡ Fast and lightweight processing
-🤖 Scalable for custom gesture training

🛠️ Tech Stack
-Python
-OpenCV
-NumPy
-TensorFlow / PyTorch
-MediaPipe

# Clone the repository
git clone https://github.com/sachinjaat98/Hand_Gesture_Recognition.git

# Navigate to project folder
cd Hand_Gesture_Recognition

# Install dependencies
pip install -r requirements.txt

python main.py

-Make sure your webcam is connected
-Perform gestures in front of the camera
-The system will detect and classify gestures in real-time


📂 Project Structure
Hand_Gesture_Recognition/
│── dataset/           # Training data
│── models/            # Saved models
│── src/               # Source code
│── main.py            # Entry point
│── requirements.txt   # Dependencies
│── README.md

📊 How It Works
-Capture video from webcam
-Detect hand region using computer vision
-Extract features from hand landmarks/images
-Pass features to trained model
-Predict and display gesture

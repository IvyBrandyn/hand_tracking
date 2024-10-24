> **Note:** This project serves as a personal space for continuous skill development, so it may be in a state of flux or broken at times due to ongoing, incremental updates. I created it to showcase the kinds of things I enjoy working on, offering prospective employers a glimpse into my passion for hands-on technical problem solving.


# Hand Tracking, Gesture Recognition, and AI Training Framework

This project uses Python and Google’s Mediapipe library to perform real-time hand tracking, gesture recognition, and introduces a foundation for AI training based on facial tracking.

## Real-Time Hand Tracking
- Implemented a real-time hand tracking script using Python, Mediapipe, and OpenCV.
- Detects up to two hands and displays 21 landmarks for each hand.

## AI Training with Face Tracking (Beta)
- A framework for AI training based on real-time face tracking using Mediapipe.
- Detects facial landmarks and expressions, providing data that can be used to train machine learning models for facial expression recognition.
  
## Features
- Real-time hand tracking using Mediapipe.
- Detection of basic hand landmarks.
- Gesture recognition for common hand signs (e.g., Thumbs Up, Peace).
- Beta support for face tracking to enable AI-driven applications.

## Project Structure
- `hand_tracking.py`: Main control script for hand tracking and gesture recognition.
- `gestures/`: Folder containing gesture detection logic.
  - `thumbs_up.py`: Detects the "Thumbs Up" gesture.
  - `peace_sign.py`: Detects the "Peace Sign" gesture.
- `AI/`: Contains initial framework for AI training.
  - `ai_controller.py`: Main script to manage AI-based data generation and training.
  - `dataset_visualizer.py`: Visualizes training data.
  - `generate_data.py`: Generates data for training AI based on facial landmarks.
- `facial_expressions/`: Scripts for detecting facial expressions for AI model training.

## Getting Started
1. Clone this repository: `<CLONE_RESPOSITORY_LOCATION>`
2. Install dependencies:
> pip install mediapipe opencv-python
3. Run the hand tracking script:
> python hand_tracking.py

## Next Steps
- Add more gestures (e.g., Ok sign, Fist).
- Integrate gesture-based control of on-screen elements.
- Expand AI training with more facial expression data.
- Create real-time AI-driven applications based on facial tracking.

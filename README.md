# Hand Tracking and Gesture Recognition

This project uses Python and Google’s Mediapipe library to perform real-time hand tracking and gesture recognition.

## Real-Time Hand Tracking
- Implemented a basic real-time hand tracking script using Python, Mediapipe, and OpenCV.
- Detects up to two hands and displays 21 landmarks for each hand

## Features
- Real-time hand tracking using Mediapipe
- Detection of basic hand landmarks
- Gesture recognition for common hand signs (e.g., Thumbs Up, Peace)

## Project Structure
- `hand_tracking.py`: Main control script for hand tracking and gesture recognition.
- `gestures/`: Folder containing separate gesture detection logic.
  - `thumbs_up.py`: Contains logic for detecting the "Thumbs Up" gesture.
  - `peace_sign.py`: Contains logic for detecting the "Peace Sign" gesture.

## Getting Started
1. Clone this repository:
<CLONE_RESPOSITORY_LOCATION>
2. Install dependencies:
`pip install mediapipe opencv-python`
3. Run the `hand_tracking.py` file:
`python hand_tracking.py`

## Next Steps
- [ ] Add more gestures (Ok sign, Fist, etc.)
- [ ] Integrate gesture-based control of on-screen elements

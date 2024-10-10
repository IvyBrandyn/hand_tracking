import cv2
import mediapipe as mp
from gestures.thumbs_up import is_thumb_up      # Import thumbs up detection
from gestures.peace_sign import is_peace_sign   # Import peace sign detection


# Initialize Mediapipe's Hand class and drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Set up the webcam capture
cap = cv2.VideoCapture(0)   # Use 0 for the default camera

# Configure the Mediapipe Hands object
with mp_hands.Hands(
    static_image_mode=False,        # Detect hands in a video stream
    max_num_hands=2,                # Track up to 2 hands
    min_detection_confidence=0.7,   # Minimum confidence for hand detection
    min_tracking_confidence=0.7) as hands:

    while cap.isOpened():
        # Read each frame from the webcam
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame from webcam.")
            break

        # Flip the image for a mirror effect (selfie-view)
        frame = cv2.flip(frame, 1)

        # Convert the BGR image to RGB (Mediapipe expects RGB)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame and detect hands
        results = hands.process(frame_rgb)

        # If hand landmarks are detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks and connections on the frame
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Check for the "Thumbs Up" gesture
                if is_thumb_up(hand_landmarks):
                    # Display "Thumbs Up!" text on the frame
                    cv2.putText(frame, 'Thumbs Up!', (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

                # Check for the "Peace Sign" gesture
                if is_peace_sign(hand_landmarks):
                    cv2.putText(frame, 'Peace Sign!', (30, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        # Display the annotated frame
        cv2.imshow('Hand Tracking', frame)

        # Exit on pressing 'q'
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()

import cv2
import mediapipe as mp
from gestures.thumbs_up import is_thumb_up
from gestures.peace_sign import is_peace_sign

class HandTracker:
    def __init__(self, max_num_hands_=2, min_detection_confidence_=0.7, min_tracking_confidence_=0.7):
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=max_num_hands_,
            min_detection_confidence=min_detection_confidence_,
            min_tracking_confidence=min_tracking_confidence_
        )
    
    def process_frame(self, raw_frame, render_frame):
        # Convert the frame to RGB and process it with Mediapipe
        raw_frame_rgb = cv2.cvtColor(raw_frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(raw_frame_rgb)

        # Draw hand landmarks if detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(render_frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

                # Check for the "Thumbs Up" gesture
                if is_thumb_up(hand_landmarks):
                    # Display "Thumbs Up!" text on the frame
                    cv2.putText(render_frame, 'Thumbs Up!', (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

                # Check for the "Peace Sign" gesture
                if is_peace_sign(hand_landmarks):
                    cv2.putText(render_frame, 'Peace Sign!', (30, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)


    def stop(self):
        # Release resources if needed
        pass

import cv2
import mediapipe as mp
from gestures.thumbs_up import is_thumb_up
from gestures.peace_sign import is_peace_sign


class HandTrackerPipeline:
    def __init__(
        self, max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.7
    ):
        self._max_num_hands = max_num_hands
        self._min_detection_confidence = min_detection_confidence
        self._min_tracking_confidence = min_tracking_confidence
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.initialize_hands()

    def initialize_hands(self):
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=self._max_num_hands,
            min_detection_confidence=self._min_detection_confidence,
            min_tracking_confidence=self._min_tracking_confidence,
        )

    @property
    def max_num_hands(self):
        return self._max_num_hands

    @max_num_hands.setter
    def max_num_hands(self, value):
        # Type check to ensure the value is an integer
        if not isinstance(value, int):
            raise ValueError("max_num_hands must be an integer.")
        if value < 1:
            raise ValueError("max_num_hands must be at last 1.")
        self._max_num_hands = value
        self.initialize_hands()

    @property
    def min_detection_confidence(self):
        return self._min_detection_confidence

    @min_detection_confidence.setter
    def min_detection_confidence(self, value):
        # Type check to ensure the value is a float
        if not isinstance(value, float):
            raise ValueError("min_detection_confidence must be a float")
        if value < 0.0:
            raise ValueError("min_detection_confidence must be >= 0.0")
        self._min_detection_confidence = value
        self.initialize_hands()

    @property
    def min_tracking_confidence(self):
        return self._min_tracking_confidence

    @min_tracking_confidence.setter
    def min_tracking_confidence(self, value):
        # Type check to ensure the value is a float
        if not isinstance(value, float):
            raise ValueError("min_tracking_confidence must be a float")
        if value < 0.0:
            raise ValueError("min_tracking_confidence must be >= 0.0")
        self._min_tracking_confidence = value
        self.initialize_hands()

    def process_frame(self, raw_frame, render_frame):
        # Convert the frame to RGB and process it with Mediapipe
        raw_frame_rgb = cv2.cvtColor(raw_frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(raw_frame_rgb)

        # Draw hand landmarks if detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(
                    render_frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
                )

                # Check for the "Thumbs Up" gesture
                if is_thumb_up(hand_landmarks):
                    # Display "Thumbs Up!" text on the frame
                    cv2.putText(
                        render_frame,
                        "Thumbs Up!",
                        (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 0),
                        2,
                        cv2.LINE_AA,
                    )

                # Check for the "Peace Sign" gesture
                if is_peace_sign(hand_landmarks):
                    cv2.putText(
                        render_frame,
                        "Peace Sign!",
                        (30, 100),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (255, 0, 0),
                        2,
                        cv2.LINE_AA,
                    )

    def stop(self):
        # Release resources if needed
        pass

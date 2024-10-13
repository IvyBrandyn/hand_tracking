import cv2
import mediapipe as mp


class BodyTrackerPipeline:
    def __init__(
        self,
        model_complexity=1,
        min_detection_confidence=0.3,
        min_tracking_confidence=0.3,
    ):
        self._model_complexity = model_complexity
        self._min_detection_confidence = min_detection_confidence
        self._min_tracking_confidence = min_tracking_confidence
        self.mp_pose = mp.solutions.pose
        self.mp_drawing = mp.solutions.drawing_utils
        self.initialize_pose()

    def initialize_pose(self):
        self.pose = self.mp_pose.Pose(
            static_image_mode=False,
            model_complexity=self._model_complexity,
            min_detection_confidence=self._min_detection_confidence,
            min_tracking_confidence=self._min_tracking_confidence,
        )

    @property
    def model_complexity(self):
        return self._model_complexity

    @model_complexity.setter
    def model_complexity(self, value):
        # Type check to ensure the value is an integer
        if not isinstance(value, int):
            raise ValueError("model_complexity must be an integer.")
        if value < 0:
            raise ValueError("model_complexity must be at last 1.")
        self._model_complexity = value
        self.initialize_pose()

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
        self.initialize_pose()

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
        self.initialize_pose()

    def process_frame(self, raw_frame, render_frame):
        # Convert the frame to RGB and process it with Mediapipe
        raw_frame_rgb = cv2.cvtColor(raw_frame, cv2.COLOR_BGR2RGB)
        results = self.pose.process(raw_frame_rgb)

        # Draw pose landmarks if detected
        if results.pose_landmarks:
            self.mp_drawing.draw_landmarks(
                render_frame, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS
            )

    def stop(self):
        # Release resources if needed
        pass

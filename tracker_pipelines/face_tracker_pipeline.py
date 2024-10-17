import cv2
import mediapipe as mp
from facial_expressions.smiling import is_smiling
from facial_expressions.smiling import draw_debug_landmarks

class FaceTrackerPipeline:
    def __init__(
        self, max_num_faces=2, min_detection_confidence=0.5, min_tracking_confidence=0.5
    ):
        # Initialize Mediapipe Face Mesh
        self._max_num_faces = max_num_faces
        self._min_detection_confidence = min_detection_confidence
        self._min_tracking_confidence = min_tracking_confidence
        self.mp_face_mesh = mp.solutions.face_mesh
        self.mp_drawing = mp.solutions.drawing_utils
        self.initialize_face_mesh()

    def initialize_face_mesh(self):
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            static_image_mode=False,
            max_num_faces=self._max_num_faces,
            min_detection_confidence=self._min_detection_confidence,
            min_tracking_confidence=self._min_tracking_confidence,
        )

    @property
    def max_num_faces(self):
        return self._max_num_faces

    @max_num_faces.setter
    def max_num_faces(self, value):
        # Type check to ensure the value is an integer
        if not isinstance(value, int):
            raise ValueError("max_num_faces must be an integer.")
        if value < 1:
            raise ValueError("max_num_faces must be at last 1.")
        self._max_num_faces = value
        self.initialize_face_mesh()

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
        self.initialize_face_mesh()

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
        self.initialize_face_mesh()

    def process_frame(self, raw_frame, render_frame):
        # Conver the raw frame to RGB and process it with Mediapipe
        raw_frame_rgb = cv2.cvtColor(raw_frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(raw_frame_rgb)

        # Draw face landmarks on the render frame if detected
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                self.mp_drawing.draw_landmarks(
                    render_frame,
                    face_landmarks,
                    self.mp_face_mesh.FACEMESH_TESSELATION,
                    self.mp_drawing.DrawingSpec(
                        color=(80, 110, 10), thickness=1, circle_radius=1
                    ),
                    self.mp_drawing.DrawingSpec(
                        color=(80, 256, 121), thickness=1, circle_radius=1
                    ),
                )

                # Call the function to draw the debug landmarks (in smiling.py)
                draw_debug_landmarks(render_frame, face_landmarks)

                if is_smiling(face_landmarks):
                    cv2.putText(
                        render_frame,
                        "Smiling!",
                        (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 0),
                        2,
                        cv2.LINE_AA,
                    )

    def stop(self):
        # Release resources if needed
        pass

import cv2
import mediapipe as mp

class FaceTracker:
    def __init__(self, max_num_faces_=2, min_detection_confidence_=0.5, min_tracking_confidence_=0.5):
        # Initialize Mediapipe Face Mesh
        self.mp_face_mesh = mp.solutions.face_mesh
        self.mp_drawing = mp.solutions.drawing_utils
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            static_image_mode=False,
            max_num_faces=max_num_faces_,
            min_detection_confidence=min_detection_confidence_,
            min_tracking_confidence=min_tracking_confidence_,
        )

    def process_frame(self, raw_frame, render_frame):
        # Conver the raw frame to RGB and process it with Mediapipe
        raw_frame_rgb = cv2.cvtColor(raw_frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(raw_frame_rgb)

        # Draw face landmarks on the render frame if detected
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                self.mp_drawing.draw_landmarks(
                    render_frame, face_landmarks, self.mp_face_mesh.FACEMESH_TESSELATION,
                    self.mp_drawing.DrawingSpec(color=(80, 110, 10), thickness=1, circle_radius=1),
                    self.mp_drawing.DrawingSpec(color=(80, 256, 121), thickness=1, circle_radius=1)
                )

    def stop(self):
        # Release resources if needed
        pass

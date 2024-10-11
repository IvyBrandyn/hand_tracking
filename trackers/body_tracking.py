import cv2
import mediapipe as mp

class BodyTracker:
    def __init__(self, model_complexity_=1, min_detection_confidence_=0.3, min_tracking_confidence_=0.3):
        self.mp_pose = mp.solutions.pose
        self.mp_drawing = mp.solutions.drawing_utils
        self.pose = self.mp_pose.Pose(
            static_image_mode=False,
            model_complexity=model_complexity_,
            min_detection_confidence=min_detection_confidence_,
            min_tracking_confidence=min_tracking_confidence_,
        )
    
    def process_frame(self, raw_frame, render_frame):
        # Convert the frame to RGB and process it with Mediapipe
        raw_frame_rgb = cv2.cvtColor(raw_frame, cv2.COLOR_BGR2RGB)
        results = self.pose.process(raw_frame_rgb)

        # Draw pose landmarks if detected
        if results.pose_landmarks:
            self.mp_drawing.draw_landmarks(render_frame, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)
    
    def stop(self):
        # Release resources if needed
        pass

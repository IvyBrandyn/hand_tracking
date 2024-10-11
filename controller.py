import cv2
import copy
from trackers.hand_tracker import HandTracker
from trackers.body_tracking import BodyTracker
from trackers.face_tracker import FaceTracker


class Controller:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)  # Initialize the camera feed
        self.hand_tracker = HandTracker()
        self.body_tracker = BodyTracker()
        self.face_tracker = FaceTracker()
        self.stop_signal = False        # Signal to stop the tracking loop
    
    def start_tracking(self):
        while not self.stop_signal:
            ret, raw_frame = self.cap.read()
            if not ret:
                print("Failed to grab frame from camera.")
                break

            # Create a separate copy for rendering
            render_frame = copy.deepcopy(raw_frame)

            # Process the frame with both trackers using the same raw frame but render on a shared copy
            self.hand_tracker.process_frame(raw_frame, render_frame)    # Read raw, draw on render_frame
            self.body_tracker.process_frame(raw_frame, render_frame)    # Read raw, draw on render_frame
            self.face_tracker.process_frame(raw_frame, render_frame)    # Read raw, draw on render_frame

            # Display the final rendered frame (includes overlay from both trackers)
            cv2.imshow('Combined Tracking', render_frame)

            # Exit on pressing 'q'
            if cv2.waitKey(5) & 0xFF == ord('q'):
                self.stop_signal = True
                break
        
        self.stop_tracking()
    
    def stop_tracking(self):
        # Stop both trackers
        self.hand_tracker.stop()
        self.body_tracker.stop()
        self.face_tracker.stop()

        # Release camera resources and close OpenCV windows
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Initialize and start the controller
    controller = Controller()
    try:
        controller.start_tracking()
    except KeyboardInterrupt:
        print("Stopping trackers...")
        controller.stop_tracking()

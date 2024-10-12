import threading
import cv2
import copy
import json
from trackers_pipeline import TrackersPipeline
from reconfigure_modal import ReconfigureModal


class Controller:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)  # Initialize the camera feed

        # Load the tracker states from the config file
        self.config = self.load_config()

        # Initialize the TrackersPipeline
        self.trackers_pipeline = TrackersPipeline()

        # Signal to stop the tracking loop
        self.stop_signal = False

        # Start the reconfiguration modal in a separate thread
        self.reconfigure_thread = threading.Thread(target=self.start_reconfigure_modal)
        self.reconfigure_thread.start()

    def load_config(self):
        """Loads tracker states from the config.json file."""
        try:
            with open("config.json", "r") as config_file:
                config = json.load(config_file)
                return config
        except FileNotFoundError:
            print("Configuration file not found. Exiting.")
            self.stop_tracking()
    
    def start_tracking(self):
        """Main loop for capturing frames and processing pipelines."""
        while not self.stop_signal:
            ret, raw_frame = self.cap.read()
            if not ret:
                print("Failed to grab frame from camera.")
                break

            # Create a copy for rendering the processed frame
            render_frame = copy.deepcopy(raw_frame)

            # Process the frame through all enabled pipelines
            self.trackers_pipeline.process_frame(raw_frame, render_frame)

            # Display the processed frame
            cv2.imshow('Combined Pipeline Tracking', render_frame)

            # Exit on pressing 'q'
            if cv2.waitKey(5) & 0xFF == ord('q'):
                self.stop_signal = True
                break
        
        self.stop_tracking()
    
    def start_reconfigure_modal(self):
        """Create and run the reconfigure modal in a separate thread."""
        self.modal = ReconfigureModal(self.trackers_pipeline)
        self.modal.run()
    
    def stop_tracking(self):
        """Stops the tracking pipelines and releases resources."""
        self.trackers_pipeline.stop()   # Stop all pipelines

        # Close the reconfigure modal
        if hasattr(self, 'reconfigure_thread') and self.reconfigure_thread.is_alive():
            self.modal.root.quit()  # Ensure the Tkinter window is closed

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

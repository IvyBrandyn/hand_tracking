import tkinter as tk
from reconfigure_modules.hand_tracker_reconfigure import HandTrackerReconfigure
from reconfigure_modules.body_tracker_reconfigure import BodyTrackerReconfigure
from reconfigure_modules.face_tracker_reconfigure import FaceTrackerReconfigure


class ReconfigureModal:
    def __init__(self, trackers_pipeline):
        self._trackers_pipeline = (
            trackers_pipeline  # Reference to the controller to update states
        )

        # Create the Tkinter window
        self.root = tk.Tk()
        self.root.title("Pipeline Reconfiguration")

        # Set minimum size with a fixed width and dynamic height
        self.root.minsize(width=700, height=400)

        ### Tracker Pipelines Section (Enable/Disable Pipelines)
        tracker_frame = tk.LabelFrame(
            self.root, text="Tracker Pipelines", padx=10, pady=10
        )
        tracker_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        # Hand Tracker Checkbox
        self.hand_var = tk.BooleanVar(
            value=self._trackers_pipeline.pipeline_states["hand"]
        )
        self.hand_checkbox = tk.Checkbutton(
            tracker_frame,
            text="Enable Hand Tracking Pipeline",
            variable=self.hand_var,
            command=self.update_hand_tracker_pipeline_state,
        )
        self.hand_checkbox.pack(anchor=tk.W, padx=5, pady=5, fill=tk.X)

        # Body Tracker Checkbox
        self.body_var = tk.BooleanVar(
            value=self._trackers_pipeline.pipeline_states["body"]
        )
        self.body_checkbox = tk.Checkbutton(
            tracker_frame,
            text="Enable Body Tracking Pipeline",
            variable=self.body_var,
            command=self.update_body_tracker_pipeline_state,
        )
        self.body_checkbox.pack(anchor=tk.W, padx=5, pady=5, fill=tk.X)

        # Face Tracker Checkbox
        self.face_var = tk.BooleanVar(
            value=self._trackers_pipeline.pipeline_states["face"]
        )
        self.face_checkbox = tk.Checkbutton(
            tracker_frame,
            text="Enable Face Tracking Pipeline",
            variable=self.face_var,
            command=self.update_face_tracker_pipeline_state,
        )
        self.face_checkbox.pack(anchor=tk.W, padx=5, pady=5, fill=tk.X)

        ### Hand Tracker Pipeline Section
        hand_tracker_frame = tk.LabelFrame(
            self.root, text="Hand Tracker Pipeline", padx=10, pady=10
        )
        hand_tracker_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        # Hand Tracker Pipeline Reconfiguration
        self.hand_tracker_reconfigure = HandTrackerReconfigure(
            hand_tracker_frame, self._trackers_pipeline.hand_tracking_pipeline
        )

        ### Body Tracker Pipeline Section
        body_tracker_frame = tk.LabelFrame(
            self.root, text="Body Tracker Pipeline", padx=10, pady=10
        )
        body_tracker_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        # Body Tracker Pipeline Reconfiguration
        self.body_tracker_reconfigure = BodyTrackerReconfigure(
            body_tracker_frame, self._trackers_pipeline.body_tracking_pipeline
        )

        ### Face Tracker Pipeline Section
        face_tracker_frame = tk.LabelFrame(
            self.root, text="Face Tracker Pipeline", padx=10, pady=10
        )
        face_tracker_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        # Face Tracker Pipeline Reconfiguration
        self.face_tracker_reconfigure = FaceTrackerReconfigure(
            face_tracker_frame, self._trackers_pipeline.face_tracking_pipeline
        )

        # Apply Changes Button (Optional)
        self.apply_button = tk.Button(
            self.root, text="Apply Changes", command=self.apply_changes
        )
        self.apply_button.pack(pady=10)

    # HandTracker methods
    def update_hand_tracker_pipeline_state(self):
        # Update the state of the hand tracker in the controller
        self._trackers_pipeline.update_pipeline_state("hand", self.hand_var.get())

    # BodyTracker methods
    def update_body_tracker_pipeline_state(self):
        # Update the state of the body tracker in the controller
        self._trackers_pipeline.update_pipeline_state("body", self.body_var.get())

    # FaceTracker methods
    def update_face_tracker_pipeline_state(self):
        # Update the state of the face tracker in the controller
        self._trackers_pipeline.update_pipeline_state("face", self.face_var.get())

    def apply_changes(self):
        # You can add any additional logic here for applying changes if needed
        pass

    def run(self):
        # Start the Tkinter main loop
        self.root.mainloop()

    def quit(self):
        self.root.quit()
        self.root.destroy()

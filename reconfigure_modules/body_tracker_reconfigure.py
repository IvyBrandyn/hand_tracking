import tkinter as tk


class BodyTrackerReconfigure:
    def __init__(self, root, body_tracker_pipeline):
        self._body_tracker_pipeline = body_tracker_pipeline
        self._root = root

        # Model Complexity Slider
        tk.Label(self._root, text="Model Complexity").pack(anchor=tk.W)
        self.model_complexity_slider = tk.Scale(self._root, from_=0, to=2, orient=tk.HORIZONTAL, command=self.update_model_complexity)
        self.model_complexity_slider.set(self._body_tracker_pipeline.model_complexity)
        self.model_complexity_slider.pack(anchor=tk.W)

        # Min Detection Confidence Slider
        tk.Label(self._root, text="Min Detection Confidence").pack(anchor=tk.W)
        self.min_detection_confidence_slider = tk.Scale(self._root, from_=0.0, to=1.0, resolution=0.1, orient=tk.HORIZONTAL, command=self.update_min_detection_confidence)
        self.min_detection_confidence_slider.set(self._body_tracker_pipeline.min_detection_confidence)
        self.min_detection_confidence_slider.pack(anchor=tk.W)

        # Min Tracking Confidence Slider
        tk.Label(self._root, text="Min Tracking Confidence").pack(anchor=tk.W)
        self.min_tracking_confidence_slider = tk.Scale(self._root, from_=0.0, to=1.0, resolution=0.1, orient=tk.HORIZONTAL, command=self.update_min_tracking_confidence)
        self.min_tracking_confidence_slider.set(self._body_tracker_pipeline.min_tracking_confidence)
        self.min_tracking_confidence_slider.pack(anchor=tk.W)

    def update_model_complexity(self, value):
        # Update the model_complexity parameter in the BodyTracker
        self._body_tracker_pipeline.model_complexity = int(value)
    
    def update_min_detection_confidence(self, value):
        # Update the min_detection_confidence parameter in the BodyTracker
        self._body_tracker_pipeline.min_detection_confidence = float(value)
    
    def update_min_tracking_confidence(self, value):
        # Update the min_tracking_confidence parameter in the BodyTracker
        self._body_tracker_pipeline.min_tracking_confidence = float(value)

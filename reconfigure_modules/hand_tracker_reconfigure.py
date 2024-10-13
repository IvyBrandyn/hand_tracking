import tkinter as tk


class HandTrackerReconfigure:
    def __init__(self, root, hand_tracker_pipeline):
        self._hand_tracker_pipeline = hand_tracker_pipeline
        self._root = root

        # Max Number of Hands Slider
        tk.Label(self._root, text="Max Number of Hands").pack(anchor=tk.W)
        self.max_hands_slider = tk.Scale(
            self._root,
            from_=1,
            to=4,
            orient=tk.HORIZONTAL,
            command=self.update_max_num_hands,
        )
        self.max_hands_slider.set(self._hand_tracker_pipeline.max_num_hands)
        self.max_hands_slider.pack(anchor=tk.W, padx=5, pady=5, fill=tk.X)

        # Min Detection Confidence Slider
        tk.Label(self._root, text="Min Detection Confidence").pack(anchor=tk.W)
        self.min_detection_confidence_slider = tk.Scale(
            self._root,
            from_=0.0,
            to=1.0,
            resolution=0.1,
            orient=tk.HORIZONTAL,
            command=self.update_min_detection_confidence,
        )
        self.min_detection_confidence_slider.set(
            self._hand_tracker_pipeline.min_detection_confidence
        )
        self.min_detection_confidence_slider.pack(
            anchor=tk.W, padx=5, pady=5, fill=tk.X
        )

        # Min Tracking Confidence Slider
        tk.Label(self._root, text="Min Tracking Confidence").pack(anchor=tk.W)
        self.min_tracking_confidence_slider = tk.Scale(
            self._root,
            from_=0.0,
            to=1.0,
            resolution=0.1,
            orient=tk.HORIZONTAL,
            command=self.update_min_tracking_confidence,
        )
        self.min_tracking_confidence_slider.set(
            self._hand_tracker_pipeline.min_tracking_confidence
        )
        self.min_tracking_confidence_slider.pack(anchor=tk.W, padx=5, pady=5, fill=tk.X)

    def update_max_num_hands(self, value):
        # Update the max_num_hands parameter in the HandTracker
        self._hand_tracker_pipeline.max_num_hands = int(value)

    def update_min_detection_confidence(self, value):
        # Update the min_detection_confidence parameter in the HandTracker
        self._hand_tracker_pipeline.min_detection_confidence = float(value)

    def update_min_tracking_confidence(self, value):
        # Update the min_tracking_confidence parameter in the HandTracker
        self._hand_tracker_pipeline.min_tracking_confidence = float(value)

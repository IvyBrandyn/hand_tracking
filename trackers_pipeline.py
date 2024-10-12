from tracker_pipelines.hand_tracker_pipeline import HandTrackerPipeline
from tracker_pipelines.body_tracker_pipeline import BodyTrackerPipeline
from tracker_pipelines.face_tracker_pipeline import FaceTrackerPipeline

class TrackersPipeline:
    def __init__(self) -> None:
        # Initialize pipelines for hand, body, and face
        self.hand_tracking_pipeline = HandTrackerPipeline()
        self.body_tracking_pipeline = BodyTrackerPipeline()
        self.face_tracking_pipeline = FaceTrackerPipeline()

        # Keep track of the state of each pipeline
        self.pipeline_states = {
            "hand": True,
            "body": True,
            "face": True
        }

    def process_frame(self, raw_frame, render_frame):
        # Process the frame with each pipeline based on the state
        if self.pipeline_states["hand"]:
            self.hand_tracking_pipeline.process_frame(raw_frame, render_frame)
        if self.pipeline_states["body"]:
            self.body_tracking_pipeline.process_frame(raw_frame, render_frame)
        if self.pipeline_states["face"]:
            self.face_tracking_pipeline.process_frame(raw_frame, render_frame)
    
    def update_pipeline_state(self, pipeline_name, state):
        # Enable or disable a specific pipeline
        if pipeline_name in self.pipeline_states:
            self.pipeline_states[pipeline_name] = state
    
    def stop(self):
        # Stop all pipelines
        self.hand_tracking_pipeline.stop()
        self.body_tracking_pipeline.stop()
        self.face_tracking_pipeline.stop()


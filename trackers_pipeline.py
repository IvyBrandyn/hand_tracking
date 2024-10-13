from tracker_pipelines.hand_tracker_pipeline import HandTrackerPipeline
from tracker_pipelines.body_tracker_pipeline import BodyTrackerPipeline
from tracker_pipelines.face_tracker_pipeline import FaceTrackerPipeline


class TrackersPipeline:

    def __init__(self, config):
        # Initialize hand tracker pipeline with config values
        self.hand_tracking_pipeline = HandTrackerPipeline(
            max_num_hands=config["hand_tracker_pipeline"]["max_num_hands"],
            min_detection_confidence=config["hand_tracker_pipeline"][
                "min_detection_confidence"
            ],
            min_tracking_confidence=config["hand_tracker_pipeline"][
                "min_tracking_confidence"
            ],
        )

        # Initialize body tracker pipeline with config values
        self.body_tracking_pipeline = BodyTrackerPipeline(
            min_detection_confidence=config["body_tracker_pipeline"][
                "min_detection_confidence"
            ],
            min_tracking_confidence=config["body_tracker_pipeline"][
                "min_tracking_confidence"
            ],
        )

        # Initialize face tracker pipeline with config values
        self.face_tracking_pipeline = FaceTrackerPipeline(
            min_detection_confidence=config["face_tracker_pipeline"][
                "min_detection_confidence"
            ],
            min_tracking_confidence=config["face_tracker_pipeline"][
                "min_tracking_confidence"
            ],
        )

        # Initialize pipeline states based on config file
        self.pipeline_states = {
            "hand": config["tracker_pipelines"]["hand"],
            "body": config["tracker_pipelines"]["body"],
            "face": config["tracker_pipelines"]["face"],
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

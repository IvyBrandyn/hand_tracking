import threading
import logging
from gui.dataset_generation_gui import DatasetGenerationGUI
from generate_data import generate_data_for_all_emotions


BASE_DATASET_PATH = "/home/ivy/Documents/portfolio/hand_tracking/AI/data_sets/AffectNet"
OUTPUT_PATH = "/home/ivy/Documents/portfolio/hand_tracking/AI/generated_data"

class AIController:
    def __init__(self):
        self.gui = DatasetGenerationGUI(
            controller=self
        )  # Link the GUI to the controller
        self.is_running = False  # Tracks the status of the task
        self.logger = logging.getLogger()  # Create a logger for the AIController
        self.setup_logging()

    def setup_logging(self):
        """
        Sets up logging for the dataset generation process, directs logs to the GUI.
        """
        # Set up the logger and default level
        self.logger.setLevel(logging.DEBUG)

        # Log to the GUI window through the controller's GUI log updater
        logging_handler = self.LoggingToGUIHandler(self)
        logging_handler.setLevel(logging.DEBUG)
        self.logger.addHandler(logging_handler)

    def set_log_level(self, log_level):
        """
        Sets the log level dynamically from the GUI.
        :param log_level: The logging level to set (DEBUG, INFO, etc.)
        """
        self.logger.setLevel(log_level)
        self.gui.update_log(f"Log level set to {log_level}")

    def start_gui(self):
        """
        Starts the GUI and handle dataset generation via the controller
        """
        self.gui.run()

    def start_generation(self):
        """
        Starts the dataset generation process.
        """
        if not self.is_running:
            self.is_running = True
            self.gui.update_log("Starting dataset generation...")
            # Run dataset generation in a separate thread to avoid GUI freezing
            thread = threading.Thread(target=self.run_generation_data)
            thread.start()

    def run_generation_data(self):
        """
        Run the generation process using generate_data.py
        """
        try:
            generate_data_for_all_emotions(BASE_DATASET_PATH, OUTPUT_PATH)
            self.gui.update_log("Dataset generation completed successfully!")
        except Exception as e:
            self.gui.update_log(f"Error during dataset generation: {e}")
        finally:
            self.is_running = False

    class LoggingToGUIHandler(logging.Handler):
        """
        Custom logging handler to send log messages to the GUI's log display
        """

        def __init__(self, controller):
            super().__init__()
            self.controller = controller

        def emit(self, record):
            log_entry = self.format(record)
            self.controller.gui.update_log(log_entry + "")


if __name__ == "__main__":
    controller = AIController()
    controller.start_gui()

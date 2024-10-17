import threading
from gui.dataset_generation_gui import DatasetGenerationGUI
from generate_data import generate_data_for_all_emotions


class AIController:
    def __init__(self):
        self.gui = DatasetGenerationGUI(
            controller=self
        )  # Link the GUI to the controller
        self.is_running = False  # Tracks the status of the task

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
            self.gui.update_log("Starting dataset generation...\n")
            # Run dataset generation in a separate thread to avoid GUI freezing
            thread = threading.Thread(target=self.run_generation_data)
            thread.start()

    def run_generation_data(self):
        """
        Run the generation process using generate_data.py
        """
        try:
            base_dataset_path = (
                "/home/ivy/Documents/portfolio/hand_tracking/AI/data_sets/AffectNet"
            )
            output_path = (
                "/home/ivy/Documents/portfolio/hand_tracking/AI/generated_data"
            )
            generate_data_for_all_emotions(
                base_dataset_path, output_path, log_callback=self.gui.update_log
            )
            self.gui.update_log("Dataset generation completed successfully!\n")
        except Exception as e:
            self.gui.update_log(f"Error during dataset generation: {e}\n")
        finally:
            self.is_running = False


if __name__ == "__main__":
    controller = AIController()
    controller.start_gui()

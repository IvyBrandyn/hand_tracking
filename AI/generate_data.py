import os
import cv2
import mediapipe as mp
import pandas as pd
import datetime
import logging

# Initialize Mediapipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1)


def ensure_directory_exists(directory):
    """
    Ensure that the given directory and its parent directories exist.
    If they don't exist, create them.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
        logging.info(f"Directory created: {directory}")
    else:
        logging.debug(f"Directory already exists: {directory}")


def extract_facial_landmarks(image_path):
    """
    Extract 468 facial landmarks from the image using Mediapipe.
    :param image_path: Path to the image file.
    :return: A flattened list of x and y coordinates for each landmark point.
    """
    image_name = os.path.basename(image_path)
    logging.debug(f"Processing {image_name}...")

    img = cv2.imread(image_path)
    if img is None:
        logging.warning(f"Failed to load image: {image_name}")
        return None

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(img_rgb)

    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0]
        landmarks_points = [[landmark.x, landmark.y] for landmark in landmarks.landmark]
        logging.debug(f"Landmarks extracted from {image_name}")
        return landmarks_points
    else:
        logging.warning(f"No face detected in {image_name}")
        return None


def create_landmarks_csv(base_dataset_path, output_csv_dir, emotion):
    """
    Process all images in the folder, extract facial landmarks, and store them in a csv.
    The 'emotion' parameter is the label for all data in the folder.
    """
    image_files = [
        f
        for f in os.listdir(base_dataset_path)
        if f.endswith((".png", ".jpg", ".jpeg"))
    ]

    data = []

    # Ensure output directory exists
    ensure_directory_exists(output_csv_dir)
    logging.info(f"Output directory: {output_csv_dir}")

    for file in image_files:
        image_path = os.path.join(base_dataset_path, file)
        logging.debug(f"Processing image: {file}")

        landmarks = extract_facial_landmarks(image_path)

        if landmarks:
            flattened_landmarks = [coord for point in landmarks for coord in point]
            data.append([emotion] + flattened_landmarks)

    # If data exists, save it to CSV
    if data:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        csv_filename = f"landmarks_{emotion}_{timestamp}.csv"
        csv_path = os.path.join(output_csv_dir, csv_filename)

        # Create the DataFrame
        column_names = ["emotion"] + [
            f"{i}_{coord}" for i in range(468) for coord in ["x", "y"]
        ]
        df = pd.DataFrame(data, columns=column_names)

        # Save DataFrame to CSV
        df.to_csv(csv_path, index=False)
        logging.info(f"CSV file created: {csv_filename}, saved to {csv_path}")
    else:
        logging.warning(f"No data to save for emotion {emotion}. No CSV created.")


def generate_data_for_dataset(base_dataset_path, generated_data_base_path, emotion):
    """
    Generate landmark data for a specific dataset folder and save to a structured output folder.
    """
    logging.info(f"Generating data for emotion: {emotion}")
    relative_dataset_path = os.path.relpath(base_dataset_path, start=base_dataset_path)

    # Define the output folder based on the relative path
    output_csv_dir = os.path.join(generated_data_base_path, relative_dataset_path)

    # Ensure the directory exists (creates it if necessary)
    ensure_directory_exists(output_csv_dir)

    # Create CSV in the corresponding output directory
    create_landmarks_csv(base_dataset_path, output_csv_dir, emotion)


def generate_data_for_all_emotions(base_dataset_path, generated_data_base_path):
    """
    Iterate through the 'train' folder and process each emotion folder
    """
    # Iterate through the 'train' folder
    train_folder = os.path.join(base_dataset_path, "train")
    emotion_folders = [
        f
        for f in os.listdir(train_folder)
        if os.path.isdir(os.path.join(train_folder, f))
    ]

    for emotion in emotion_folders:
        emotion_folder_path = os.path.join(train_folder, emotion)
        logging.info(f"Processing emotion folder: {emotion}")
        generate_data_for_dataset(
            emotion_folder_path, generated_data_base_path, emotion
        )

import os
import cv2
import mediapipe as mp
import matplotlib.pyplot as plt

# Initialize Mediapipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

# Initialize the Mediapipe face mesh instance
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=True, max_num_faces=1, min_detection_confidence=0.5
)


def get_image_files(folder_path):
    """
    Retrieves a list of image files in the given folder.
    """
    image_extensions = [".jpg", ".jpeg", ".png"]
    return [
        f
        for f in sorted(os.listdir(folder_path))
        if os.path.splitext(f)[-1].lower() in image_extensions
    ]


def load_affectnet_image(image_path):
    """
    Load an image from the AffectNet dataset using OpenCV
    """
    img = cv2.imread(image_path)
    if img is None:
        print(f"Failed to load image {image_path}")
        return None
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def apply_face_mesh(image):
    """
    Apply Mediapipe face mesh on the input image.
    """
    # Convert image to RGB format required by Mediapipe
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image to extract face landmarks
    results = face_mesh.process(image_rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Draw face landmarks
            mp_drawing.draw_landmarks(
                image,
                face_landmarks,
                mp_face_mesh.FACEMESH_TESSELATION,
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
                mp_drawing.DrawingSpec(
                    color=(80, 110, 10), thickness=1, circle_radius=1
                ),
            )
    return image


def visualize_affectnet_image_with_mesh(image_path):
    """
    Load an image from AffectNet, apply the Mediapipe face mesh, and display the results.
    """
    # Load the image
    image = load_affectnet_image(image_path)

    if image is None:
        return

    # Apply Mediapipe face mesh to the image
    image_with_mesh = apply_face_mesh(image)

    # Convert the image back to BGR for OpenCV display
    image_bgr = cv2.cvtColor(image_with_mesh, cv2.COLOR_RGB2BGR)

    # Plot the result
    cv2.imshow("AffectNet Image with Mesh", image_bgr)


def image_navigator(folder_path):
    """
    Navigate through the images in the folder with 'n' for next and 'p' for previous.
    """
    image_files = get_image_files(folder_path)
    current_idx = 0

    while True:
        if current_idx < 0:
            current_idx = 0
        if current_idx >= len(image_files):
            current_idx = len(image_files) - 1

        # Full path to the image
        image_path = os.path.join(folder_path, image_files[current_idx])
        print(f"Displaying {image_files[current_idx]}")

        # Visualize the current image
        visualize_affectnet_image_with_mesh(image_path)

        # Wait for user input
        key = cv2.waitKey(0) & 0xFF

        if key == ord("n"):
            current_idx += 1
        elif key == ord("p"):
            current_idx -= 1
        elif key == ord("q"):
            print("Exiting.")
            break

        # Close all OpenCV windows
        cv2.destroyAllWindows()


# Path to the AffectNet dataset folder (adjust this path to your dataset)
affectnet_path = (
    "/home/ivy/Documents/portfolio/hand_tracking/data_sets/AffectNet/train/0/"
)

# Start navigating through images
image_navigator(affectnet_path)

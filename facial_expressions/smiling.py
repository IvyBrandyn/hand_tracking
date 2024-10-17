import cv2
import mediapipe as mp

mp_face_landmarks = mp.solutions.face_mesh.FaceMesh


def is_smiling(face_landmarks):
    """
    Detects if the person is smiling by comparing the mouth landmarks

    :param face_landmarks: The facial landmarks for a single face
    :return True if smiling, False othewise.
    """
    left_lip_corner = face_landmarks.landmark[61]
    right_lip_corner = face_landmarks.landmark[291]
    upper_lip = face_landmarks.landmark[13]
    lower_lip = face_landmarks.landmark[14]

    # Cheek landmarks to detect elevation
    left_cheek = face_landmarks.landmark[130]
    right_cheek = face_landmarks.landmark[243]

    # Horizontal and vertical distances
    horizontal_lip_distance = abs(left_lip_corner.x - right_lip_corner.x)
    vertical_lip_distance = abs(upper_lip.y - lower_lip.y)

    # Lip curvature
    lip_midpoint_y = (left_lip_corner.y + right_lip_corner.y) / 2
    upper_lip_curvature = lip_midpoint_y - lower_lip.y
    lower_lip_curvature = lower_lip.y - lip_midpoint_y

    # Smile ratio
    smile_ratio = horizontal_lip_distance / vertical_lip_distance

    # Cheek elevation: checks if cheeks are raised
    cheek_elevation = (lip_midpoint_y - ((left_cheek.y + right_cheek.y) / 2)) > 0

    # Conditions for a smile
    is_upward_curved = upper_lip_curvature > 0 and lower_lip_curvature > 0

    if vertical_lip_distance < 0.02:  # Closed mouth
        return smile_ratio > 1.3 and is_upward_curved and cheek_elevation
    else:  # Open mouth
        return smile_ratio > 1.5 and is_upward_curved and cheek_elevation


def draw_debug_landmarks(image, face_landmarks):
    """
    Draws large red dots on the specified facial landmarks for debugging.
    :param image: The frame to display
    :param face_landmarks: The facial landmarks for a single face.
    """
    # Define a list of the landmark indices you want to track (for example lips, cheeks, eyes, etc.)
    landmarks_to_track = [61, 291, 13, 14, 130, 243]

    for idx in landmarks_to_track:
        x = int(face_landmarks.landmark[idx].x * image.shape[1])
        y = int(face_landmarks.landmark[idx].y * image.shape[0])

        # Draw a large red dot for visibility
        cv2.circle(image, (x, y), 5, (0, 0, 255), -1)

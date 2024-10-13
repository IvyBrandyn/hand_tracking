import mediapipe as mp

mp_face_landmarks = mp.solutions.face_mesh.FaceMesh


def is_smiling(face_landmarks):
    """
    Detects if the person is smiling by comparing the mouth landmarks

    :param face_landmarks: The facial landmarks for a single face
    :return True if smiling, False othewise.
    """
    # Extract key mouth landmarks (lip corners and edges)
    left_lip_corner = face_landmarks.landmark[61]
    right_lip_corner = face_landmarks.landmark[291]
    upper_lip = face_landmarks.landmark[13]
    lower_lip = face_landmarks.landmark[14]

    # Calculate the horizontal distance between the lip corners
    horizontal_lip_distance = abs(left_lip_corner.x - right_lip_corner.x)

    # Calculate the vertical distance between the upper and lower lip
    vertical_lip_distance = abs(upper_lip.y - lower_lip.y)

    # Set a threshold for smile detection based on the ratio of distances
    smile_ratio = horizontal_lip_distance / vertical_lip_distance

    # Adjust the threshold based on open-mouth vs closed-mouth smiles
    if vertical_lip_distance < 0.02:  # Small threshold for closed-mouth smiles
        return (
            smile_ratio > 0.5
        )  # Adjust this value for better detection of closed smiles
    else:
        return smile_ratio > 1.8  # Threshold for open-mouth smiles

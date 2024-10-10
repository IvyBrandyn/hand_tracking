import mediapipe as mp
import numpy as np

mp_hand_landmarks = mp.solutions.hands.HandLandmark

def get_relative_positions(hand_landmarks):
    """
    Converts hand landmark positions to a relative coordinate system centered on the wrist.
    :param hand_landmarks: The landmarks for a single hand.
    :return: A dictionary of relative positions.
    """
    """found_landmarks = hand_landmarks.landmark

    wrist = found_landmarks[mp_hand_landmarks.WRIST]

    # Create a dictionary with relative x and y positions
    relative_positions = {}
    for landmark in mp_hand_landmarks:
        relative_positions[landmark] = {
            'x': found_landmarks[landmark].x - wrist.x,
            'y': found_landmarks[landmark].y - wrist.y
        }
    return relative_positions"""
    found_landmarks = hand_landmarks.landmark

    # Extract coordinates of key landmarks
    wrist = found_landmarks[mp_hand_landmarks.WRIST]
    wrist_array = np.array([wrist.x, wrist.y])

    middle_mcp = found_landmarks[mp_hand_landmarks.MIDDLE_FINGER_MCP]
    middle_mcp_array = np.array([middle_mcp.x, middle_mcp.y])

    # Define the y-axis (wrist to middle MCP)
    y_axis = middle_mcp_array - wrist_array
    y_axis /= np.linalg.norm(y_axis)    # Normalize

    # Define the x-axis as perpendicular to the y-axis
    # In 2D, we can get a perpendicular vector by swapping coordinates and inverting one
    x_axis = np.array([-y_axis[1], y_axis[0]])

    # Create a transformation matrix from world to wrist frame
    transformation_matrix = np.array([x_axis, y_axis]).T    # 2x2 matrix

    # Function to transform a point to the wrist frame
    def transform_to_wrist_frame(landmark):
        point_vector = np.array([found_landmarks[landmark].x, found_landmarks[landmark].y]) - wrist_array
        relative_vector = transformation_matrix.dot(point_vector)
        return relative_vector
    
    relative_positions = {}
    for landmark in mp_hand_landmarks:
        relative_positions[landmark] = transform_to_wrist_frame(landmark)

    return relative_positions

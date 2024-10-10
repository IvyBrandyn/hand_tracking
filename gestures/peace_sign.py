import mediapipe as mp


mp_hand_landmarks = mp.solutions.hands.HandLandmark

def is_peace_sign(hand_landmarks):
    """
    Determines if the hand is in the "Peace Sign" position.
    :param hand_landmarks: The landmarks for a single hand.
    :return: True if in the peace sign position, False otherwise.
    """
    found_landmarks = hand_landmarks.landmark

    # Check the y-coordinates of the tips of the index and middle fingers
    index_tip_y = found_landmarks[mp_hand_landmarks.INDEX_FINGER_TIP].y
    middle_tip_y = found_landmarks[mp_hand_landmarks.MIDDLE_FINGER_TIP].y

    # Check the y-coordinates of the ring and pinky finger tips
    ring_tip_y = found_landmarks[mp_hand_landmarks.RING_FINGER_TIP].y
    pinky_tip_y = found_landmarks[mp_hand_landmarks.PINKY_TIP].y

    # Check if the index and middle fingers are extended
    index_extended = index_tip_y < found_landmarks[mp_hand_landmarks.INDEX_FINGER_DIP].y
    middle_extended = middle_tip_y < found_landmarks[mp_hand_landmarks.MIDDLE_FINGER_DIP].y

    # Check if the ring and pinky fingers are curled
    ring_curled = ring_tip_y > found_landmarks[mp_hand_landmarks.RING_FINGER_DIP].y
    pinky_curled = pinky_tip_y > found_landmarks[mp_hand_landmarks.PINKY_DIP].y

    # Ensure the index and middle fingers have significant gap (different from other gestures)
    index_middle_gap = abs(found_landmarks[mp_hand_landmarks.INDEX_FINGER_TIP].x - found_landmarks[mp_hand_landmarks.MIDDLE_FINGER_TIP].x) > 0.05

    # If the index and middle are extended, and the ring and pinky are not, it's a peace sign
    return index_extended and middle_extended and ring_curled and pinky_curled and index_middle_gap

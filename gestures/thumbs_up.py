import mediapipe as mp
from gestures.utils import get_relative_positions
from gestures.utils import is_palm_facing_camera


mp_hand_landmarks = mp.solutions.hands.HandLandmark

def is_thumb_up(hand_landmarks):
    """
    Determines if the thumb is in the "Thumbs Up" position.

    TODO: Current implementation fails to determine gesture without using camera frame.

    :param hand_landmarks: The landmarks for a single hand.
    :return: True if thumb is up, False otherwise.
    """
    relative_positions = get_relative_positions(hand_landmarks)

    # Get the absolute Y coordinates of the thumb tip and thumb ip in the camera frame
    thumb_tip_y = hand_landmarks.landmark[mp_hand_landmarks.THUMB_TIP].y
    thumb_ip_y = hand_landmarks.landmark[mp_hand_landmarks.THUMB_IP].y

    # Thumb's up logic: The thumb tip must be above (lower Y) than the thumb IP joint
    thumb_pointing_up = thumb_tip_y < thumb_ip_y

    if not thumb_pointing_up:
        return False

    # Check for bent thumb
    thumb_tip_rel = abs(relative_positions[mp_hand_landmarks.THUMB_TIP])
    thumb_ip_rel = abs(relative_positions[mp_hand_landmarks.THUMB_IP])
    thumb_bent = thumb_tip_rel[0] > thumb_ip_rel[0]

    # Gather finger tip and dip information to determine curl
    index_tip_rel = abs(relative_positions[mp_hand_landmarks.INDEX_FINGER_TIP])
    middle_tip_rel = abs(relative_positions[mp_hand_landmarks.MIDDLE_FINGER_TIP])
    ring_tip_rel = abs(relative_positions[mp_hand_landmarks.RING_FINGER_TIP])
    pinky_tip_rel = abs(relative_positions[mp_hand_landmarks.PINKY_TIP])

    index_dip_rel = abs(relative_positions[mp_hand_landmarks.INDEX_FINGER_DIP])
    middle_dip_rel = abs(relative_positions[mp_hand_landmarks.MIDDLE_FINGER_DIP])
    ring_dip_rel = abs(relative_positions[mp_hand_landmarks.RING_FINGER_DIP])
    pinky_dip_rel = abs(relative_positions[mp_hand_landmarks.PINKY_DIP])

    # Check if fingers are curled based on relative Y positions
    index_curled = index_tip_rel[1] < index_dip_rel[1]
    middle_curled = middle_tip_rel[1] < middle_dip_rel[1]
    ring_curled = ring_tip_rel[1] < ring_dip_rel[1]
    pinky_curled = pinky_tip_rel[1] < pinky_dip_rel[1]

    fingers_curled = index_curled and middle_curled and ring_curled and pinky_curled

    # 1 is too low of a threshold.  Min should be 3, but it is inconsistent.  :/
    if fingers_curled >= 1 and thumb_bent and thumb_pointing_up:
        return True
    else:
        return False

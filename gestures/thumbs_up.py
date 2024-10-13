import mediapipe as mp
from gestures.utils import get_relative_positions


mp_hand_landmarks = mp.solutions.hands.HandLandmark


def is_thumb_up(hand_landmarks):
    """
    Determines if the thumb is in the "Thumbs Up" position.
    :param hand_landmarks: The landmarks for a single hand.
    :return: True if thumb is up, False otherwise.
    """
    relative_positions = get_relative_positions(hand_landmarks)
    thumb_tip_rel = abs(relative_positions[mp_hand_landmarks.THUMB_TIP])
    thumb_ip_rel = abs(relative_positions[mp_hand_landmarks.THUMB_IP])
    thumb_bent = thumb_tip_rel[0] > thumb_ip_rel[0]

    index_tip_rel = abs(relative_positions[mp_hand_landmarks.INDEX_FINGER_TIP])
    middle_tip_rel = abs(relative_positions[mp_hand_landmarks.MIDDLE_FINGER_TIP])
    ring_tip_rel = abs(relative_positions[mp_hand_landmarks.RING_FINGER_TIP])
    pinky_tip_rel = abs(relative_positions[mp_hand_landmarks.PINKY_TIP])

    index_dip_rel = abs(relative_positions[mp_hand_landmarks.INDEX_FINGER_DIP])
    middle_dip_rel = abs(relative_positions[mp_hand_landmarks.MIDDLE_FINGER_DIP])
    ring_dip_rel = abs(relative_positions[mp_hand_landmarks.RING_FINGER_DIP])
    pinky_dip_rel = abs(relative_positions[mp_hand_landmarks.PINKY_DIP])

    index_curled = index_tip_rel[1] < index_dip_rel[1]
    middle_curled = middle_tip_rel[1] < middle_dip_rel[1]
    ring_curled = ring_tip_rel[1] < ring_dip_rel[1]
    pinky_curled = pinky_tip_rel[1] < pinky_dip_rel[1]

    fingers_curled = index_curled and middle_curled and ring_curled and pinky_curled

    return thumb_bent and fingers_curled


def is_thumb_down(hand_landmarks):
    """
    Determines if the thumb is in the "Thumbs Down" position.
    :param hand_landmarks: The landmarks for a single hand.
    :return: True if thumb is down, False otherwise.
    """
    relative_positions = get_relative_positions(hand_landmarks)
    thumb_tip_rel = abs(relative_positions[mp_hand_landmarks.THUMB_TIP])
    thumb_ip_rel = abs(relative_positions[mp_hand_landmarks.THUMB_IP])
    thumb_bent = thumb_tip_rel[0] > thumb_ip_rel[0]

    index_tip_rel = abs(relative_positions[mp_hand_landmarks.INDEX_FINGER_TIP])
    middle_tip_rel = abs(relative_positions[mp_hand_landmarks.MIDDLE_FINGER_TIP])
    ring_tip_rel = abs(relative_positions[mp_hand_landmarks.RING_FINGER_TIP])
    pinky_tip_rel = abs(relative_positions[mp_hand_landmarks.PINKY_TIP])

    index_dip_rel = abs(relative_positions[mp_hand_landmarks.INDEX_FINGER_DIP])
    middle_dip_rel = abs(relative_positions[mp_hand_landmarks.MIDDLE_FINGER_DIP])
    ring_dip_rel = abs(relative_positions[mp_hand_landmarks.RING_FINGER_DIP])
    pinky_dip_rel = abs(relative_positions[mp_hand_landmarks.PINKY_DIP])

    index_curled = index_tip_rel[1] < index_dip_rel[1]
    middle_curled = middle_tip_rel[1] < middle_dip_rel[1]
    ring_curled = ring_tip_rel[1] < ring_dip_rel[1]
    pinky_curled = pinky_tip_rel[1] < pinky_dip_rel[1]

    fingers_curled = index_curled and middle_curled and ring_curled and pinky_curled

    return thumb_bent and fingers_curled

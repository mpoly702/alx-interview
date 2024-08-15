#!/usr/bin/python3
"""Method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """Determines if boxes can be unlocked"""
    unlocked = {0}
    keys = {0}

    while keys:
        n_key = keys.pop()
        for key in boxes[n_key]:
            if key < len(boxes) and key not in unlocked:
                unlocked.add(key)
                keys.add(key)
        if len(unlocked) == len(boxes):
            return True

    return len(unlocked) == len(boxes)

#!/usr/bin/python3


"""UTF-8 validation module"""


def validUTF8(data):
    """
    Confirms if a given list of int represents a valid UTF-8 encoding

    Args:
    Data: List of int
    Returns:
    Bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_by = 0

    m1 = 1 << 7
    m2 = 1 << 6

    for u in data:
        byte = u & 0xFF

        if num_by == 0:
            m = 1 << 7
            while m & byte:
                num_by += 1
                m = m >> 1

            if num_by == 0:
                continue

            if num_by == 1 or num_by > 4:
                return False
        else:
            if not (byte & m1 and not (byte & m2)):
                return False

        num_by -= 1

    return num_by == 0

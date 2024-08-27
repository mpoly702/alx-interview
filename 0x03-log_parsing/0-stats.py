#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""


import sys


def get_results(statusCodes, fileSize):
    """Get statistics"""
    print("File size: {:d}".format(fileSize))
    for statusCode, u in sorted(statusCodes.items()):
        if u:
            print("{:s}: {:d}".format(statusCode, u))


def process_line(line, statusCodes, fileSize):
    """Process a single line to update metrics"""
    info = line.split()
    try:
        sc = info[-2]
        if sc in statusCodes:
            statusCodes[sc] += 1
        fileSize += int(info[-1])
    except (IndexError, ValueError):
        pass
    return fileSize


if __name__ == '__main__':
    statusCodes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    fileSize = 0
    lns = 0

    try:
        for ln in sys.stdin:
            lns += 1
            fileSize = process_line(ln, statusCodes, fileSize)
            if lns % 10 == 0:
                get_results(statusCodes, fileSize)
        get_results(statusCodes, fileSize)
    except KeyboardInterrupt:
        get_results(statusCodes, fileSize)
        raise

import codecs
import math
import os
import sys

import qrcode

import zookeeper

as_string = {32: " ", 220: "▄", 223: "▀", 219: "█"}

SCROLL_WARNING = """
WARNING: Scrolls only display 15 lines at a time. Your QR code requires {}
lines (plus 2 for a border). Scanning may difficult if not impossible in this
format.
"""


def main():
    characters = {
        (0, 0): 32,
        (0, 255): 220,
        (255, 0): 223,
        (255, 255): 219,
    }

    if len(sys.argv) != 2:
        url = "https://museumofzzt.com/file/z/zzt.zip"
    else:
        url = sys.argv[1]
    img = qrcode.make(url, box_size=1, border=0)

    board = zookeeper.Board(populate=True, title="QR2BRD", message="Generated with QR2ZZT")
    board.stats[0].x = 60
    board.stats[0].y = 25

    # Fill the board
    for x in range(0, 1500):
        board.elements[x] = zookeeper.Element(21, 15)

    player = zookeeper.Element(4, 31)
    board.elements[1499] = player
    empty = zookeeper.Element(0, 0)
    board.elements[689] = empty

    # Draw the QR code
    h_offset = (60 - img.width) // 2
    v_offset = ((25 - (img.height // 2)) // 2) * 60
    element_idx = h_offset + v_offset

    as_text = "$" + ("█"*(img.width + 2)) + "\n"
    for y in range(0, img.height, 2):
        as_text += "$█"
        for x in range(0, img.width):
            upper_pixel = img.getpixel((x, y))
            if y + 1 == img.height:
                lower_pixel = 255
            else:
                lower_pixel = img.getpixel((x, y+1))

            pair = (upper_pixel, lower_pixel)

            # Having to do both of these is a Zookeeper issue.
            text = zookeeper.Element(53, characters[pair])
            text.character = characters[pair]
            as_text += as_string[text.character]

            board.elements[element_idx] = text
            element_idx += 1

        # Move to the left edge again
        element_idx += 60 - img.width
        as_text += "█\n"

    board.export("output")
    print("Exported.")

    # Save the QR code
    if math.ceil(img.height / 2) > 13:
        print(SCROLL_WARNING.format(math.ceil(img.height / 2)))

    as_text += "$" + ("█"*(img.width + 2)) + "\n"
    as_text += "$" + url + "\n"
    with codecs.open("output.txt", "w", "cp437") as fh:
        fh.write(as_text)
    return True


if __name__ == "__main__":
    main()

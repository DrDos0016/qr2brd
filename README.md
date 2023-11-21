# QR2ZZT

A QR Code creator for ZZT.

Originally made in 2018. Published in 2023 to prevent it from being completely
lost. It is very barebones.

## Requirements

- [Pillow](https://pypi.org/project/Pillow/)
- [qrcode](https://pypi.org/project/qrcode/)
- [Zookeeper](https://github.com/DrDos0016/zookeeper/)

## Usage

`python3 qr2brd.py url`

This will output two files `output.brd` and `output.txt`.

The `BRD` file is a valid ZZT board with the QR Code centered. An invisible
watermark for the tool is inserted into the board's "message" field, but
will not be displayed to players.

The `TXT` file is encoded in a format that KevEdit can import into an
object with `Alt+I` in the program's code editor. This format may not be
suitable for other editors.

## Notes

Message windows in ZZT may not be tall enough to display your QR code
entirely at once. You can usually get away with a single line being off-screen,
but beyond that the code is likely unreadable. You may benefit from using a
URL-shortening service such as TinyURL when encoding.

If your code is too tall to fit, a warning message is printed when running the
script.

If you use this script in a ZZT release, crediting Dr. Dos and QR2ZZT itself
is encouraged, though not required.

This tool received the bare minimum attention to continue working in 2023 and
is unlikely to receive future updates.

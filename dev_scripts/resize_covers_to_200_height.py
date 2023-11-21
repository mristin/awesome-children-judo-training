"""Resize all the cover images to 200 pixels."""

import itertools
import os
import pathlib
import sys

from PIL import Image

def main() -> int:
    """Execute the main routine."""
    this_path = pathlib.Path(os.path.realpath(__file__))
    covers_dir = this_path.parent.parent / "covers"

    for pth in sorted(
            itertools.chain(
                covers_dir.glob("**/*.jpg"),
                covers_dir.glob("**/*.jpeg"),
                covers_dir.glob("**/*.png"),
            )
    ):
        with Image.open(str(pth)) as image:
            image.thumbnail((200, 200))
            image.save(str(pth))

    return 0


if __name__ == "__main__":
    sys.exit(main())

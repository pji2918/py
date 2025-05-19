import os
import string
from pathlib import Path

if Path.exists(Path(f"{Path.home()}/Downloads/alltexts.txt")):
    os.remove(f"{Path.home()}/Downloads/alltexts.txt")

with open(f"{Path.home()}/Downloads/alltexts.txt", mode="w+", encoding="utf-8") as f:
    f.write(
        f"{string.ascii_letters}{string.digits}{string.punctuation} "
        + "".join([chr(i) for i in range(0xAC00, 0xD7A4)])
        + "".join([chr(i) for i in range(0x3131, 0x3163)])
    )

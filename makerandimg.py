import random
import time

from PIL import Image

image = Image.new(mode="RGBA", size=(300, 300))
pix = image.load()
random.seed(time.time())

for i in range(image.size[0]):
    for j in range(image.size[1]):
        if random.randint(0, 1) == 1:
            pix[i, j] = (255, 255, 255)  # type: ignore
        else:
            pix[i, j] = (0, 0, 0)  # type: ignore

        # pix[i, j] = (  # type: ignore
        #     random.randint(0, 255),
        #     random.randint(0, 255),
        #     random.randint(0, 255),
        # )

image.show()

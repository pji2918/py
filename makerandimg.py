from PIL import Image
import random
import datetime

image = Image.new(mode="RGBA", size=(3000, 3000))
pix = image.load()

for i in range(image.size[0]):
    for j in range(image.size[1]):
        random.seed(
            datetime.datetime.strptime(
                datetime.datetime.now().isoformat(sep=" ", timespec="seconds"),
                "%Y-%m-%d %H:%M:%S",
            ).timestamp()
        )
        if random.randint(0, 1) == 1:
            pix[i, j] = (255, 255, 255)
        else:
            pix[i, j] = (0, 0, 0)

image.save("test.png", format="PNG")
image.show()

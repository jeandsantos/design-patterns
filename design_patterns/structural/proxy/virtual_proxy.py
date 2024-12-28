"""Virtual Proxy.

A virtual proxy is a proxy that appears to be the underlying object.
A virtual proxy is masquerading the underlying functionality and may not have the underlying functionality.
"""


class Bitmap:
    def __init__(self, filename: str):
        self.filename = filename
        print(f"Loading image from {self.filename}")

    def draw(self):
        print(f"Drawing image from {self.filename}")


class LazyBitmap:
    def __init__(self, filename: str):
        self.filename = filename
        self._bitmap: Bitmap | None = None

    def draw(self):
        if self._bitmap is None:
            self._bitmap = Bitmap(self.filename)
        self._bitmap.draw()


def draw_image(image: Bitmap):
    print("About to draw image")
    image.draw()
    print("Done drawing image")


def main():
    bitmap = Bitmap("image.png")
    draw_image(bitmap)

    print()

    lazy_bitmap = LazyBitmap("lazy_image.png")
    draw_image(lazy_bitmap)


if __name__ == "__main__":
    main()
    # output:
    # Loading image from image.png       <-- Image is eagerly loaded
    # About to draw image
    # Drawing image from image.png
    # Done drawing image
    #
    # About to draw image
    # Loading image from lazy_image.png  <-- Image is only loaded when it is needed
    # Drawing image from lazy_image.png
    # Done drawing image

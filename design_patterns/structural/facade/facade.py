class Buffer:
    def __init__(self, width: int = 30, height: int = 20):
        self.width = width
        self.height = height
        self.buffer = [" " * (width * height)]

    def __getitem__(self, item):
        return self.buffer.__getitem__(item)

    def write(self, text: str):
        self.buffer += text


class Viewport:
    def __init__(self, buffer: Buffer = Buffer()):
        self.buffer = buffer
        self.offset = 0

    def get_char_at(self, index: int) -> str:
        return self.buffer[index + self.offset]

    def append(self, text: str):
        self.buffer.write(text)


class Console:
    """Facade for the buffer and viewport."""

    def __init__(self):
        buffer = Buffer()
        self.current_viewport = Viewport(buffer)
        self.buffers = [buffer]
        self.viewports = [self.current_viewport]

    def write(self, text: str):
        self.current_viewport.buffer.write(text)

    def get_char_at(self, index: int) -> str:
        return self.current_viewport.get_char_at(index)


if __name__ == "__main__":
    console = Console()
    console.write("Hello")
    char = console.get_char_at(0)
    print(char)

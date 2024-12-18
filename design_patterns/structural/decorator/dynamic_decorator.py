"""Dynamic decorator."""

import os


class FileWithLogging:
    def __init__(self, file):
        self.file = file

    def writelines(self, lines):
        self.file.writelines(lines)
        print(f"Wrote {len(lines)} lines")

    def __iter__(self):
        return self.file.__iter__()

    def __next__(self):
        return self.file.__next__()

    def __getattr__(self, item):
        return getattr(self.__dict__["file"], item)

    def __setattr__(self, key, value):
        if key == "file":
            self.__dict__[key] = value
        else:
            setattr(self.__dict__["file"], key, value)

    def __delattr__(self, item):
        delattr(self.__dict__["file"], item)


def main():
    try:
        file = FileWithLogging(open("test.txt", "w"))
        file.writelines(["hello", "world"])
        file.write("test")
    finally:
        file.close()
        os.remove("test.txt")


if __name__ == "__main__":
    main()

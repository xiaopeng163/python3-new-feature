from typing import Tuple, List

class Photo:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.tags = []    # change to self.tags: List[str] = []

    def get_dimensions(self) -> Tuple[int, int]:
        return (self.width, self.height)

if __name__ == "__main__":

    photos = [
        Photo(10, 20),
        Photo(30, 40)
    ]
    photos.append('abc')   # change to photos.append(Photo(40, 50))

"""
Helper functions to make our programming easier.
"""
import pygame

from pathlib import Path

BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


def load_image(filename):
    """
    Load an image from the images folder
    and return the pygame image object.
    """
    base_path = Path(__file__).parent
    image_path = str(base_path / "images" / filename)
    return pygame.image.load(image_path)

"""
Helper functions to make our programming easier.
"""
import os.path
import pygame

BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


def load_image(filename):
    """
    Load an image from the images folder
    and return the pygame image object.
    """
    base_path = os.path.dirname(__file__)
    image_path = os.path.join(base_path, filename)
    return pygame.image.load(image_path)

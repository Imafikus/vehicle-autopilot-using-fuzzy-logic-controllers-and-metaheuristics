from pygame.math import Vector2
import math

IMAGE_DIR = "img"
IMAGE_NAME = "car.png"

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_POSITION = (0, 100)

CAR_WIDTH = 40
CAR_HEIGHT = 20
CAR_POS_X = 10
CAR_POS_Y = 400
CAR_ANGLE = -45

PATH_COLOR = (155, 100, 200, 255)
SCREEN_COLOR = (100, 100, 100, 255)
GOAL = Vector2(SCREEN_WIDTH-10, SCREEN_HEIGHT/2)
from RoundPeg import RoundPeg
from SquarePeg import SquarePeg
import math


class SquarePegAdapter(RoundPeg, SquarePeg):
    def __init__(self, w):
        self.width = w
        self.radius = w * math.sqrt(2) / 2


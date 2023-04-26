from constants import *


class MiniCube:
    def __init__(self, x, y, z):
        self.colors = {
            F: (COLOR_WHITE if x == 1 else COLOR_NONE),
            R: (COLOR_RED if z == 1 else COLOR_NONE),
            U: (COLOR_BLUE if y == 1 else COLOR_NONE),
            B: (COLOR_YELLOW if x == 3 else COLOR_NONE),
            L: (COLOR_ORANGE if z == 3 else COLOR_NONE),
            D: (COLOR_GREEN if y == 3 else COLOR_NONE)
        }
        self.rotation_cases = {
            F: [u, l, d, r],
            R: [u, f, d, b],
            U: [f, r, b, l],
            B: [u, r, d, l],
            L: [u, b, d, f],
            D: [f, l, b, r]
        }

    def _move(self, l1, l2, l3, l4):
        """
        turn the mini cube in some direction,
        4 sided are given, we should do this circle:
        l1 <- l2
        |     ^
        v     |
        l4 -> l3
        """
        temp = self.colors[l1]
        self.colors[l1] = self.colors[l2]
        self.colors[l2] = self.colors[l3]
        self.colors[l3] = self.colors[l4]
        self.colors[l4] = temp

    def move(self, rotation_type):
        self._move(*self.rotation_cases[rotation_type])

    def __str__(self):
        ret = f"|{self.colors[U]}|\n"
        ret += f"|{self.colors[F]}"
        ret += f"|{self.colors[R]}"
        ret += f"|{self.colors[B]}"
        ret += f"|{self.colors[L]}|\n"
        ret += f"|{self.colors[D]}|"
        return ret

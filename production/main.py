print("Oh boy...")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D1, board.D0)
keyboard.row_pins = (board.D3, board.D2)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D]
]

if __name__ == '__main__':
    keyboard.go()

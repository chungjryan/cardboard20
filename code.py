print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP16, board.GP17, board.GP14, board.GP13,)
keyboard.row_pins = (board.GP15,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.KP_0, KC.NUMLOCK, KC.KP_DOT, KC.ENTER ]
]

if __name__ == '__main__':
    keyboard.go()


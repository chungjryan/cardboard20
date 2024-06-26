print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP22, board.GP3, board.GP7, board.GP11,)
keyboard.row_pins = (board.GP16, board.GP17, board.GP18, board.GP19, board.GP20,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.NUMLOCK, KC.KP_SLASH, KC.KP_ASTERISK, KC.KP_MINUS,
        KC.KP_7, KC.KP_8, KC.KP_9, KC.KP_PLUS,
        KC.KP_4, KC.KP_5, KC.KP_6, KC.KP_PLUS,
        KC.KP_1, KC.KP_2, KC.KP_3, KC.KP_ENTER,
        KC.KP_0, KC.KP_0, KC.KP_DOT, KC.KP_ENTER,
    ]
]

if __name__ == '__main__':
    keyboard.go()

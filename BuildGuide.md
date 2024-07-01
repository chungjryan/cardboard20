## Materials
1. Cardboard20 Chassis
2. Raspberri Pi Pico (Or any Microcontroller)
3. Switches and Keycaps (20 ct.)
4. Electrical Wire
5. Diodes (1n4148)
6. Solder
   
## Tools
1. Soldering Iron
2. Cutting Tool (X-acto Knife Recommended)
3. Adhesive

# Step 1: Cardboard20 Chassis
First, print out the [stencil.](https://github.com/chungjryan/cardboard20/blob/master/stencil_printout.pdf) 
Then, adhere it to cardboard and cut according to the guidelines. Don't fold the tabs in yet, if we leave shaping it til the end, the wiring process will be easier. 


# Step 2: Wiring
I followed [this](https://geekhack.org/index.php?topic=87689.0) handwiring guide. A matrix scheme isn't necessary, but is cleaner to work with. 

# Step 3: Folding
Fold the tabs inwards and tape/glue to the other flap to form the wedge shape

# Step 4: Rpi Pico Programming
Download the latest [micropython firmware](https://micropython.org/download/RPI_PICO/). 
Install it onto the Pi by holding the firmware button while plugging it in, then dragging the .UF2 file into the Pico's directory

Next, download [KMK Firmware](https://github.com/KMKfw/kmk_firmware/tree/main), and copy over boot.py and the kmk folder into the Pico's home directory. 

There should be a file called code.py already in the directory, which is how we will edit out layout. 
There is a sample code.py [provided](https://github.com/chungjryan/cardboard20/blob/master/code.py)
The only section of the code that concerns us as of now is this:

```
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
```
the column pins should be ordered in terms of switch position from left to right, and the rows should be ordered from top to bottom. 
The keymap can be configured in any way desired using the [kmk keycodes](https://github.com/qmk/qmk_firmware/blob/master/docs/keycodes.md)




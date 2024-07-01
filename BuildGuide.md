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

# Step 3: Rpi Pico Programming
Download the latest [micropython firmware](https://micropython.org/download/RPI_PICO/). 
Install it onto the Pi by holding the firmware button while plugging it in, then dragging the .UF2 file into the Pico's directory

Next, download [KMK Firmware](https://github.com/KMKfw/kmk_firmware/tree/main), and copy over boot.py and the kmk folder into the Pico's home directory. 

There should be a file called code.py, which is how we will edit out layout. 



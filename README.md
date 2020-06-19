# rgb-megabugs
Megabugs on an Adafruit six 64x32 (6mm pitch) RGB grid.

That's six of these babies:
https://www.adafruit.com/product/2276

That makes a 128x96 pixel display -- exactly the same as megabugs on the CoCo.

Adafruit tutorial:<br>
https://learn.adafruit.com/adafruit-rgb-matrix-bonnet-for-raspberry-pi/

Bonnet:<br>
https://www.adafruit.com/product/3211

Multiple panels:<br>
https://github.com/hzeller/rpi-rgb-led-matrix#panel-connection

If I am reading this right:
  - `led-rows=32` Each panel has 32 rows
  - `led-cols=64` Each panel has 64 columns
  - `led-chains=2` Each chain has 2 panels (128x32)
  - `led-parallel=3` Three chains (128x96)
  
https://github.com/hzeller/rpi-rgb-led-matrix/blob/master/wiring.md

# The Frame

![](art/frame.jpg)

Exact dimension of front for black LED acrylic from TAP Plastics:

30+1/4" x 22+5/8

# Three PI version

![](art/threepi.jpg)

# The installed demos

Rebuild everything with default "regular". This wipes out the custom defaults provided by the
adafruit bonet install.

```
make clean
make
```

Disable the sound module on the pi (can still use USB sound cards):

`dtparam=audio=off` in `/boot/config.txt`

```
sudo ./demo -D0 --led-cols=64 --led-rows=32 --led-chain=2 --led-parallel=3 --led-no-hardware-pulse
```

Still doesn't work for me. I have to use "no hardware pulse" or I get long color bar flickers.


import sys
import time
import numpy
import signal
import datetime
import pixelarized
import unicornhat as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(180)
unicorn.brightness(0.2)
numpy.random.rand(*unicorn.get_shape())
unicorn.show()


def draw_pixels(element, offset_x, offset_y, color):
    y = 0
    for element_slice in element:
        for x in [x for x, char in enumerate(element_slice) if char == "█"]:
            unicorn.set_pixel(x + offset_x, y + offset_y, *color)
        y += 1


def killing_me_softly(signal, frame):
    unicorn.off()
    sys.exit(0)


signal.signal(signal.SIGTERM, killing_me_softly)
while True:
    hour = datetime.datetime.now().hour
    if hour > 12:
        hour -= 12
    minute = datetime.datetime.now().minute // 10

    draw_pixels(pixelarized.numbers[hour],
                1 if hour in [10, 11, 12] else 3, 2,
                (255, hour * 36, 0))

    for m in range(minute):
        draw_pixels(pixelarized.highlight, 7, 6 - m, (255, 255, 0))

    unicorn.show()
    time.sleep(5)
    unicorn.off()

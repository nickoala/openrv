import sensor, image

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize( same as application )
sensor.skip_frames(time=2000)

while True:
    img = sensor.snapshot() \
                .lens_corr( as tuned ) \
                # .rotation_corr( ... )

    # draw crosshair to align with floor origin

    y = (img.height() * 19) // 20
    img.draw_line(0, y, img.width(), y, color=(255, 0, 0))

    x = img.width() // 2
    img.draw_line(x, 0, x, img.height(), color=(255, 0, 0))

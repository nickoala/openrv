import sensor, image

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize( same as application )
sensor.skip_frames(time=2000)

while True:
    img = sensor.snapshot() \
                .lens_corr(1.8) \
                # .rotation_corr( ... )

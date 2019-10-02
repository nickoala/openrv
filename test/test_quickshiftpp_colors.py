import sensor, image
import rv.quickshiftpp

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time=2000)

while True:
    img = sensor.snapshot()

    x_step, y_step = img.width() // 6, img.height() // 6

    # a grid of points to sample
    points = [(x,y) for x in range(x_step // 2, img.width(), x_step)
                    for y in range(y_step // 2, img.height(), y_step)]

    colors = [img.get_pixel(*p) for p in points]

    # By sampling a grid of points and clustering them, we find out roughly
    # what colors a scene is composed of.

    clusters, modes = rv.quickshiftpp.cluster(colors,
                                              k=8,
                                              beta=0.3,
                                              return_modes=True)

    for cluster, mode, number in zip(clusters, modes, range(0, len(modes))):
        for index in cluster:
            x, y = points[index]

            # Draw a cross at each sample point with its cluster's mode color.
            # The color may be very close to background and barely visible.
            img.draw_cross(x, y, colors[mode], thickness=3)

            # Draw cluster number next to sample point
            img.draw_string(x, y, str(number))

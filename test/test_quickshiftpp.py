import rv.quickshiftpp

values = [
    (1, 0),
    (2, 1),
    (3, 2),
    (3, 3),
    (3, 4),
    (4, 5),

    (6, 6),
    (9, 7),
    (11, 8),
    (23, 9),
    (36, 10),
    (48, 11),
]

t = 3
p = rv.quickshiftpp.find_threshold_position(t, values)
print(t, '->', p)

t = 3.5
p = rv.quickshiftpp.find_threshold_position(t, values)
print(t, '->', p)

t = 4
p = rv.quickshiftpp.find_threshold_position(t, values)
print(t, '->', p)

t = 4.1
p = rv.quickshiftpp.find_threshold_position(t, values)
print(t, '->', p)

t = 10
p = rv.quickshiftpp.find_threshold_position(t, values)
print(t, '->', p)

t = 36
p = rv.quickshiftpp.find_threshold_position(t, values)
print(t, '->', p)

t = 40
p = rv.quickshiftpp.find_threshold_position(t, values)
print(t, '->', p)

t = 50
p = rv.quickshiftpp.find_threshold_position(t, values)
print(t, '->', p)


points = [
    [1, 1],
    [1.0, 1.2],
    [0.9, 1.1],
    [0.95, 0.99],

    [3.3, 3.0],

    [5.0, 8.2],
    [5.5, 7.9],
    [4.8, 8.1],
    [5.1, 7.7],
]

clusters = rv.quickshiftpp.cluster(points,
                                   k=2,
                                   beta=0.2)
print(clusters)

clusters, modes = rv.quickshiftpp.cluster(points,
                                          k=2,
                                          beta=0.2,
                                          return_modes=True)
print(clusters)
print(modes)

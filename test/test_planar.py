from rv.planar import Planar
import vec

H = [
    [ 3.14916496e+01, -9.79038178e+02,  1.03951636e+05],
    [ 7.57939015e+02, -3.31912533e+01, -5.86807545e+04],
    [ 2.06572544e-01,  2.03579263e+00,  1.00000000e+00],
]

image_points = [
    [83, 109],
    [70, 100],
    [51,  92],
    [93, 100],
    [101, 86],
    [119, 62],
    [43,  67],
    [117, 75],
    [49,  71],
]

paper_squares = [
    [0,    0],
    [2,   -2],
    [4,   -6],
    [2,    2],
    [6,    4],
    [16,  10],
    [14, -10],
    [10,   8],
    [12,  -8],
]

                     # 290 mm / 15 sqaures
paper_points = [vec.mul(q, 290/15) for q in paper_squares]

offset = [305, 0]    # floor origin is 305 mm in front
world_points = [vec.add(p, offset) for p in paper_points]

p = Planar(H, offset=offset)

# Should be equal
print(world_points)
print(p.project(image_points))

# Should be equal
print(image_points)
print(p.project(world_points, reverse=True))

# Make sure H did not get changed
print(world_points)
print(p.project(image_points))

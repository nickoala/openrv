from functools import reduce
import math
import numpy as np
import click

def read_points(f):
    def point_pair(line):
        a, b, c, d = map(float, line.split())
        return [a, b], [c, d]

    def append_point_pair(value, line):
        p, q = point_pair(line)
        return value[0] + [p], value[1] + [q]

    return reduce(append_point_pair, f, ([], []))

def scale_batch(points, factor):
    return [[x * factor for x in p] for p in points]

def stack(src, dest):
    def rows(s, d):
        x, y = s
        u, v = d
        return [[-x, -y, -1, 0, 0, 0, u*x, u*y, u],
                [0, 0, 0, -x, -y, -1, v*x, v*y, v]]

    return np.array(reduce(
            lambda value, element: value + rows(*element), zip(src, dest), []))

def centroid_and_average_distance(points):
    centroid = (
        sum([p[0] for p in points]) / len(points),
        sum([p[1] for p in points]) / len(points))

    def distance_to_centroid(p):
        cx, cy = centroid
        x, y = p
        return math.sqrt((x - cx) ** 2 + (y - cy) ** 2)

    avgd = sum([distance_to_centroid(p) for p in points]) / len(points)

    return centroid, avgd

def make_normalizer_pair(c, d):
    sqrt2 = math.sqrt(2)
    cx, cy = c

    translate = np.array([
                    [1, 0, -cx],
                    [0, 1, -cy],
                    [0, 0,   1]])
    scale = np.array([
                    [sqrt2 / d, 0, 0],
                    [0, sqrt2 / d, 0],
                    [0,         0, 1]])
    normalizer = np.dot(scale, translate)

    translate = np.array([
                    [1, 0, cx],
                    [0, 1, cy],
                    [0, 0,  1]])
    scale = np.array([
                    [d / sqrt2, 0, 0],
                    [0, d / sqrt2, 0],
                    [0,         0, 1]])
    denormalizer = np.dot(translate, scale)

    return normalizer, denormalizer

def homogeneous_transform(m, p):
    q = np.dot(m, p+[1])
    return q[:-1] / q[-1]

def normalize_points(points):
    centroid, avg_distance = centroid_and_average_distance(points)
    normalizer, denormalizer = make_normalizer_pair(centroid, avg_distance)
    normalized = [homogeneous_transform(normalizer, p) for p in points]

    return normalized, normalizer, denormalizer


@click.command()
@click.argument('file', type=click.File())
@click.option('-unit', type=float, default=1.0)
@click.option('-normalize', is_flag=True)
def main(file, unit, normalize):
    src, dest = read_points(file)
    dest = scale_batch(dest, unit)

    if normalize:
        src_in, normalizer, _ = normalize_points(src)
        dest_in, _, denormalizer = normalize_points(dest)
    else:
        src_in, dest_in = src, dest

    A = stack(src_in, dest_in)
    _, _, v = np.linalg.svd(A)

    H = np.reshape(v[-1], (3, 3))
    H = H / H[-1, -1]

    if normalize:
        H = np.dot(denormalizer, np.dot(H, normalizer))

    print(H)

    dest_out = scale_batch([homogeneous_transform(H, p) for p in src], 1/unit)

    print('--- Verify ---')
    for s,d in zip(src, dest_out):
        print('{} -> {}'.format(s, d))


if __name__ == '__main__':
    main()

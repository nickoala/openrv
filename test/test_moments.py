import rv.moments
import image, show

def print_moments(m00, cc, us, ns, hs):
    print('M00:', m00)
    print('Centroid:', cc)
    print('Central moments:', us)
    print('Normalized:', ns)
    print('Hu:', hs)

p = image.Image('/images/1.pgm')
p_translate = image.Image('/images/1_translate.pgm')
p_scale = image.Image('/images/1_scale.pgm')
p_scale_rotate = image.Image('/images/1_scale_rotate.pgm')

s = image.Image('/images/S.pgm')
s_rotate = image.Image('/images/S_rotate.pgm')

d = image.Image('/images/dark.pgm')

ms = rv.moments.hu(p, return_intermediate=True)
print_moments(*ms)

ms = rv.moments.hu(p_translate, return_intermediate=True)
print_moments(*ms)
# All moments should equal first ones.

ms = rv.moments.hu(p_scale, return_intermediate=True)
print_moments(*ms)
# Normalized central moments should equal.

ms = rv.moments.hu(p_scale_rotate, return_intermediate=True)
print_moments(*ms)
# Hu moments should equal.

ms = show.time(rv.moments.hu)(s, return_intermediate=True)
print_moments(*ms)

ms = show.time(rv.moments.hu)(s_rotate, return_intermediate=True)
print_moments(*ms)
# Hu moments should equal.

ms = show.time(rv.moments.hu)(s, roi=(50, 50, 160, 160), return_intermediate=True)
print_moments(*ms)
# Hu moments should equal.

ms = show.time(rv.moments.hu)(s_rotate, roi=(50, 50, 160, 160), return_intermediate=True)
print_moments(*ms)
# Hu moments should equal.

ms = rv.moments.hu(d, return_intermediate=True)
print_moments(*ms)
# All zeros.

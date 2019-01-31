#euler q.1
import numpy as np

nums = range(1, 1000)
z = [x for x in nums if (x % 3 == 0) | (x % 5 == 0)]
np.sum(z)


#euler q.2

z1, z2 = 1, 2
w = 2
while z2 < 4000000:
    z_tmp = z1 + z2
    z1, z2 = z2, z_tmp
    if z_tmp % 2 == 0:
        w += z_tmp

print(w)

#euler q.3

num = 600851475143
f = 2
while num != 1:
    print("dividing %s by %s" % (num, f))
    if num % f == 0:
        fact = f
        num /= f
        f += 1
    else:
        f += 1

print(fact)
##

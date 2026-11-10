# NUMPY PRACTISE AXIS & .SUM

import numpy as np

four_days_sell = np.array([
    [10, 12, 9, 15],
    [8, 7, 11, 10],
    [14, 13, 12, 16],
])

print(four_days_sell.sum(axis=0))
print(four_days_sell.sum(axis=1))
print(four_days_sell[2, 3])
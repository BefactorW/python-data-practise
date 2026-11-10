# NUMPY PRACISE ALL

import numpy as np

week_sell = [120, 95, 140, 80, 200, 170, 60]
week_sell_np = np.array(week_sell)
print(week_sell_np[0])
print(week_sell_np[-1])
print(week_sell_np[0:3])
print(week_sell_np.sum())
print(week_sell_np.mean())
print(week_sell_np[week_sell_np < week_sell_np.mean()])

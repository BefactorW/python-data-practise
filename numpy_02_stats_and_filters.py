# NUMPY PRACTISE MEAN MAX ><

import numpy as np

temp = [18, 22, 25, 19, 30]

temp_np = np.array(temp)
print(temp_np.max())
print(temp_np.mean())
print(temp_np[temp_np > 20])
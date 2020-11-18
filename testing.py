"""import matplotlib.pyplot as plt

valueX = [1, 2, 3, 4]
scoreList = [5, 0, 0, 2]
plt.plot(valueX, scoreList)
plt.xticks(range(min(valueX), max(valueX)+1))
plt.xlabel("Score number")
plt.ylabel("Score")
plt.show()"""

import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)

x = np.arange(0, 10, 0.2)
y = [2.5, 3, 1.5, ... , 7, 9]
ax.plot(x, y)
plt.show()
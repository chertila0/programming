import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import math
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyBboxPatch
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np


np.random.seed(123)
vals = np.random.randint(10, size=(7, 7))
plt.pcolor(vals, cmap='plasma')
plt.show()
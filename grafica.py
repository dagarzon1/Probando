import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0.0,5.0,100)
y=np.sin(x)
plt.plot(x,y)
plt.savefig("grafica.pdf")

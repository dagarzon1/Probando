import matplotlib.pylab as plt
 
data=np.loadtxt("fecha_mancha.dat")
plt.plot(data[:,0],data[:,1])
plt.savefig("fecha_manchas.pdf")

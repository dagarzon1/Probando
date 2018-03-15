import numpy as np
 
data=np.loadtxt("monthrg.dat", usecols=(0,1,2,3))
years=data[:,0]+(data[:,1]-1)/12.0
sunspot=data[:,3]
sunspot=sunspot[years>1900]
years=years[years>1900]
file=np.array([years, sunspot])
np.savetxt("fecha_mancha.dat",file.T)

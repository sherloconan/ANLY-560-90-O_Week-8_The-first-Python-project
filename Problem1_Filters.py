import numpy as np
import matplotlib.pyplot as plt

def fun1(omega):
    return np.real(5-2*(np.exp(2j*omega)+np.exp(-2j*omega)))

# create an arithmetic progression
domain = np.linspace(start=0, stop=np.pi, num=500)

plt.plot(domain, fun1(domain))
plt.xlabel('ω')
plt.ylabel('C(L)')
plt.xticks([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi],
           ['$0$', r'$\frac{\pi}{4}}$', r'$\frac{\pi}{2}}$', r'$\frac{3\pi}{4}}$', r'$\pi$'])
plt.show()
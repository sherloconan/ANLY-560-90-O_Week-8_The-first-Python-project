import numpy as np
import matplotlib.pyplot as plt

def fun2(omega, m):
    sum = 0
    for num in range(0,m+1):
        sum += np.real(np.exp(-1j*omega*num))
    return np.abs(sum)**2

# create an arithmetic progression
domain = np.linspace(start=0, stop=np.pi, num=500)

plt.plot(domain, fun2(domain,7))
plt.xlabel('ω (m=7)')
plt.ylabel('C(L)')
plt.xticks([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi],
           ['$0$', r'$\frac{\pi}{4}}$', r'$\frac{\pi}{2}}$', r'$\frac{3\pi}{4}}$', r'$\pi$'])
plt.show()

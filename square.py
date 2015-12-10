import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 8, 0.01)
myb = []

for i in x:
    if np.floor(i)%2 == 0:
        myb.append(1)
    else:
        myb.append(0)

y = np.array(myb)

plt.subplot(121)
plt.plot(x,y)
plt.xticks([2,4,6],("-T","0","T"))
plt.tick_params(axis='x', labelsize="15")
plt.ylim([-0.5,1.5])
plt.grid(b=True, which="major", color='black', linestyle='--')

myb = []

for i in x:
    myb.append(0.5)

yl = np.array(myb)


plt.subplot(122)
plt.plot(x,yl)
plt.xticks([2,4,6],("-T","0","T"))
plt.tick_params(axis='x', labelsize="15")
plt.ylim([-0.5,1.5])
plt.grid(b=True, which="major", color='black', linestyle='--')
plt.show()




plt.subplot(121)
plt.plot(x,y)
plt.xticks([2,4,6],("-T","0","T"))
plt.tick_params(axis='x', labelsize="15")
plt.ylim([-0.5,1.5])
plt.grid(b=True, which="major", color='black', linestyle='--')

ys = yl + 2/np.pi*np.sin(x*np.pi)


plt.subplot(122)
plt.plot(x,ys)
plt.xticks([2,4,6],("-T","0","T"))
plt.tick_params(axis='x', labelsize="15")
plt.ylim([-0.5,1.5])
plt.grid(b=True, which="major", color='black', linestyle='--')
plt.show()

plt.subplot(131)
plt.plot(x,y)
plt.xticks([2,4,6],("-T","0","T"))
plt.tick_params(axis='x', labelsize="15")
plt.ylim([-0.5,1.5])
plt.grid(b=True, which="major", color='black', linestyle='--')


ys = np.zeros_like(ys)
ys += yl
for i in range(1,4,2):
    ys += 2/(np.pi*i)*np.sin(x*np.pi*i)

plt.subplot(132)
plt.plot(x,ys)
plt.xticks([2,4,6],("-T","0","T"))
plt.tick_params(axis='x', labelsize="15")
plt.ylim([-0.5,1.5])
plt.grid(b=True, which="major", color='black', linestyle='--')

for i in range(5,100,2):
    ys += 2/(np.pi*i)*np.sin(x*np.pi*i)

plt.subplot(133)
plt.plot(x,ys)
plt.xticks([2,4,6],("-T","0","T"))
plt.tick_params(axis='x', labelsize="15")
plt.ylim([-0.5,1.5])
plt.grid(b=True, which="major", color='black', linestyle='--')
plt.show()

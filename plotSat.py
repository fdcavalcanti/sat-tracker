import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

R = 1
t = np.linspace(0,2*np.pi,100)
x = R*np.cos(t)
y = R*np.sin(t)

left = 0.1
bottom = 0.1
mid = 0.5
right = 0.9
top = 0.9

class PositionAz:
    def __init__(self, Az):
        self.Az = Az
        self.AngRad = np.pi*Az/180
        self.xPos = R*np.cos(self.AngRad)
        self.yPos = R*np.sin(self.AngRad)

az1 = PositionAz(450-50) #450 é o offset de início
az2 = PositionAz(450-160)
fig = plt.figure()

ax = fig.add_axes([0,0,1,1])
ax.text(left, mid, 'West',
        horizontalalignment='left',
        verticalalignment='bottom',
        transform=ax.transAxes)
ax.text(mid, bottom, 'South',
        horizontalalignment='center',
        verticalalignment='center',
        transform=ax.transAxes)
ax.text(right, mid, 'East',
        horizontalalignment='right',
        verticalalignment='bottom',
        transform=ax.transAxes)
ax.text(mid, top, 'North',
        horizontalalignment='center',
        verticalalignment='center',
        transform=ax.transAxes)

plt.axis('equal')
plt.grid()
plt.plot(x,y)
plt.scatter(az1.xPos,az1.yPos)
plt.scatter(az2.xPos,az2.yPos)
plt.plot([az1.xPos, az2.xPos],[az1.yPos, az2.yPos])


plt.show()

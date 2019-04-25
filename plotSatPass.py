import shared_stuff as base

def PlotSatTrack(NORAD_ID):
    urlAPI = '{}/{}/{}/{}/{}/{}/{}/&apiKey={}'.format(base.urlbase,\
    NORAD_ID,base.lat,base.long,base.elev,base.days,base.ang,base.apiKey)
    dataNOAA = requests.get(urlAPI)
    satData = dataNOAA.json()

    satPass = input('Choose satellite pass (0-end): ')
    startAz = satData.get('passes')[int(satPass)]['startAz']
    maxAz = satData.get('passes')[int(satPass)]['maxAz']
    endAz = satData.get('passes')[int(satPass)]['endAz']

    az1 = PositionAz(450-int(startAz)) #450 é o offset de início
    az2 = PositionAz(450-int(endAz))

    left = 0.1
    bottom = 0.1
    mid = 0.5
    right = 0.9
    top = 0.9

    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.text(left, mid, 'West',
            horizontalalignment='left',
            verticalalignment='bottom',
            transform=ax.transAxes)
    ax.text(mid, bottom, 'South',
            horizontalalignment='center',
            verticalalignment='center',
            transform=import matplotlib.pyplot as plt
ax.transAxes)
    ax.text(right, mid, 'East',
            horizontalalignment='right',
            verticalalignment='bottom',
            transform=ax.transAxes)
    ax.text(mid, top, 'North',
            horizontalalignment='center',
            verticalalignment='center',
            transform=ax.transAxes)

    t = np.linspace(0,2*np.pi,100)
    x = R*np.cos(t)
    y = R*np.sin(t)
    plt.figure(); plt.plot(x,y)
    plt.axis('equal'); plt.grid()
    plt.scatter(az1.xPos,az1.yPos)
    plt.scatter(az2.xPos,az2.yPos)
    plt.plot([az1.xPos, az2.xPos],[az1.yPos, az2.yPos])
    plt.title('Trajetória do Satélite')
    plt.show()

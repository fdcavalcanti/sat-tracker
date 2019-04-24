#Sat Pos Request v6
#Shows closest pass satellite satellite name

import requests
import arrow
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

lat = '-7.066'; long = '-34.84'
elev = '0'; days = '1'; ang = '25'
apiKey = 'PWH3XF-ETNDQR-2X6S3P-3ZI5'
urlbase = 'https://www.n2yo.com/rest/v1/satellite/radiopasses'
satInfo = {
    'NOAA-15': ['0','137.62 MHz APT','25338'],
    'NOAA-18': ['1','137.9125 MHz APT','28654'],
    'NOAA-19': ['2','137.1 MHz APT','33591'],
    'METEOR M2': ['3','137.1 MHz QPSK', '40069']
}

R = 1
class PositionAz:
    def __init__(self, Az):
        self.Az = Az
        self.AngRad = np.pi*Az/180
        self.xPos = R*np.cos(self.AngRad)
        self.yPos = R*np.sin(self.AngRad)

def getSatData(order):
    for name in satInfo:
        if order == name:
            urlAPI = '{}/{}/{}/{}/{}/{}/{}/&apiKey={}'.format(urlbase,\
            satInfo[name][2],lat,long,elev,days,ang,apiKey)
            dataNOAA = requests.get(urlAPI)
            satData = dataNOAA.json()
    return satData

def unixTimeSat(satData,satPass):
    firstPassUTC = satData.get('passes')[satPass]['startUTC']
    startTime = datetime.fromtimestamp(firstPassUTC)
    endTime = datetime.fromtimestamp(satData.get('passes')[satPass]['endUTC'])
    return [startTime, endTime, firstPassUTC]

def PlotSatTrack(NORAD_ID):
    urlAPI = '{}/{}/{}/{}/{}/{}/{}/&apiKey={}'.format(urlbase,\
    NORAD_ID,lat,long,elev,days,ang,apiKey)
    dataNOAA = requests.get(urlAPI)
    satData = dataNOAA.json()

    satPass = input('Choose satellite pass (0-end): ')
    startAz = satData.get('passes')[int(satPass)]['startAz']
    maxAz = satData.get('passes')[int(satPass)]['maxAz']
    endAz = satData.get('passes')[int(satPass)]['endAz']

    az1 = PositionAz(450-int(startAz)) #450 é o offset de início
    az2 = PositionAz(450-int(endAz))

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

print('                 NOAA Satellite Passes')
firstPass = 9999999999

for x in satInfo:
    satData = getSatData(x)
    totalPasses = int(satData.get('info')['passescount']);
    satName = satData.get('info')['satname']
    print('')
    print('--- ' + satName + ' at ' + satInfo[x][1] + ' ---')

    for satPass in range(totalPasses):
        timeSat = unixTimeSat(satData,satPass)
        if (timeSat[2]<firstPass):
            firstPass = timeSat[2]
            satNameCurrent = satName
        print('Pass ' + str(satPass) + ' at ' + str(timeSat[0]) + ' going ' +\
        satData.get('passes')[satPass]['startAzCompass'] + ' ' + \
        satData.get('passes')[satPass]['endAzCompass'] + ' | Max elevation: ' +\
        str(satData.get('passes')[satPass]['maxEl']) + ' ending at ' + str(timeSat[1]))

print('\nClosest pass: ' + satNameCurrent + ' at ' + str(datetime.fromtimestamp(firstPass)))
plotYN = input('\nEnter to exit, 1 to plot: ')
if plotYN == '1':
    satSelect = input('Choose satellite:\n0- NOAA-15\n1- NOAA-18\n2- NOAA-19\n-> ')
    for pos in satInfo:
        if satSelect == satInfo[pos][0]:
            PlotSatTrack(satInfo[pos][2])
else:
    print('\nGoodbye!')

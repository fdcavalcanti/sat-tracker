#N2YO API KEY: PWH3XF-ETNDQR-2X6S3P-3ZI5
#&apiKey={your API key}  no final da URL
#NOAA 18 NORAD ID 28654
#NOAA 19 NORAD ID 33591
#NOAA 15 NORAD ID 25338
import requests
import arrow
from datetime import datetime
lat = '-7.066'; long = '-34.84'
elev = '0'; days = '1'; ang = '25'
apiKey = 'PWH3XF-ETNDQR-2X6S3P-3ZI5'
urlbase = 'https://www.n2yo.com/rest/v1/satellite/radiopasses'
satlist = ['NOAA-15','NOAA-18','NOAA-19']

def getSatData(order):
    if x == satlist[0]:
        id = '25338'
        urlAPI = '{}/{}/{}/{}/{}/{}/{}/&apiKey={}'.format(urlbase,id,lat,long,elev,days,ang,apiKey)
        dataNOAA = requests.get(urlAPI)
        satData = dataNOAA.json()

    elif x == satlist[1]:
        id = '28654'
        urlAPI = '{}/{}/{}/{}/{}/{}/{}/&apiKey={}'.format(urlbase,id,lat,long,elev,days,ang,apiKey)
        dataNOAA = requests.get(urlAPI)
        satData = dataNOAA.json()

    elif x == satlist[2]:
        id = '33591'
        urlAPI = '{}/{}/{}/{}/{}/{}/{}/&apiKey={}'.format(urlbase,id,lat,long,elev,days,ang,apiKey)
        dataNOAA = requests.get(urlAPI)
        satData = dataNOAA.json()
    return satData

def unixTimeSat(satData,satPass):
    startTime = datetime.fromtimestamp(satData.get('passes')[satPass]['startUTC'])
    endTime = datetime.fromtimestamp(satData.get('passes')[satPass]['endUTC'])
    return [startTime, endTime]


for x in satlist:
    satData = getSatData(x)
    totalPasses = int(satData.get('info')['passescount']);

    print('--- ' + satData.get('info')['satname'] + '---')
    for satPass in range(totalPasses):
        timeSat = unixTimeSat(satData,satPass)
        print('Pass ' + str(satPass) + ' at ' + str(timeSat[0]) + ' going ' +\
        satData.get('passes')[satPass]['startAzCompass'] + ' ' + \
        satData.get('passes')[satPass]['endAzCompass'] + ' | Max elevation: ' +\
        str(satData.get('passes')[satPass]['maxEl']) + ' ending at ' + str(timeSat[1]))


#dataNOAA15 = requests.get('https://www.n2yo.com/rest/v1/satellite/radiopasses/25338/-7.066/-34.84/0/1/30/&apiKey=PWH3XF-ETNDQR-2X6S3P-3ZI5')
#dataNOAA18 = requests.get('https://www.n2yo.com/rest/v1/satellite/radiopasses/28654/-7.066/-34.84/0/1/30/&apiKey=PWH3XF-ETNDQR-2X6S3P-3ZI5')
#dataNOAA19 = requests.get('https://www.n2yo.com/rest/v1/satellite/radiopasses/33591/-7.066/-34.84/0/1/30/&apiKey=PWH3XF-ETNDQR-2X6S3P-3ZI5')


'''
totalPasses18 = int(passNOAA18.get('info')['passescount']);
startTime18 = datetime.fromtimestamp(passNOAA18.get('passes')[0]['startUTC']);
endTime18 = datetime.fromtimestamp(passNOAA18.get('passes')[0]['endUTC']);
'''
'''
for x in range(totalPasses18):
    print('Passagem ' + str(x) + ' do ' + passNOAA18.get('info')['satname'] +\
     ' em ' + str(startTime18) + ' UTC, com elevação máxima de ' +\
      str(passNOAA18.get('passes')[x]['maxEl']) + ' finalizando em ' + str(endTime18))
'''

#satInfo = {
#        "name": passNOAA18.get('info')['satname'],
#        "passes": passNOAA18.get('info')['passescount'],
#        "elevMax": passNOAA18.get('passes')[0]['maxEl'],
#        "startTime18": str(startTime18),
#        "startAt": passNOAA18.get('passes')[0]['startAzCompass'],
#        "endTime18": str(endTime18),
#        "endAt": passNOAA18.get('passes')[0]['endAzCompass']
#    }

#print(satStatus0)
#print('\n')
#print(satStatus0.get("info")["satid"])

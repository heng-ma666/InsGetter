## some functions that my be useful
import time
import sys

##return type: [year,mon,year-mon]
def parseTime(ct):
    print(sys.version)
    t = time.localtime(float(ct))
    year = t.tm_year
    month = t.tm_mon
    if(month<10):
        month = '0'+str(month)
    ym = str(year)+'-'+str(month)
    return [year,t.tm_mon,ym]

def parseLink(url):
    list = str(url).split('/')
    return list[-2]

def checkTime(list,time):
    for i in range(0,len(list)):
        if list[i] !=None and 'date' in list[i]:
            if list[i]['date'] != None:
                if(list[i]['date'] == time):
                    return i
    return None

parseLink('https://www.instagram.com/p/BY-CMkcA4hknsR5bHQe7bC6jEUbf3f32AHItqE0/')
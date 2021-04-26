import json
import time
from Car import CarInfo


def getConfig():
    cars = []
    with open('5824_config.json', 'r', encoding='utf-8') as cf:
        configModel = json.loads(cf.read())
        result = configModel['result']
        seriesid = result['seriesid']

        paramtypeitems = result['paramtypeitems']
        speclist = result['speclist']
        for i in range(len(speclist)):
            car = CarInfo()
            car.seriesid = seriesid
            car.specid = speclist[i]['specid']
            cars.append(car)

        for pti in range(len(paramtypeitems)):
            paramitems = paramtypeitems[pti]["paramitems"]
            for pi in range(len(paramitems)):                            
                if paramitems[pi]['name'].startswith('车型'):
                    valueitems = paramitems[pi]['valueitems']
                    for vi in range(len(valueitems)):
                        cari = list(filter(lambda x : x.specid == valueitems[vi]['specid'], cars))[0]
                        cari.name = valueitems[vi]['value']

                if paramitems[pi]['name'].startswith('厂') and len(paramitems[pi]['name']) > 100:
                    valueitems = paramitems[pi]['valueitems']
                    for vi in range(len(valueitems)):
                        cari = list(filter(lambda x : x.specid == valueitems[vi]['specid'], cars))[0]
                        cari.official_price = valueitems[vi]['value']
                
                if paramitems[pi]['id'] == 53:
                    valueitems = paramitems[pi]['valueitems']
                    for vi in range(len(valueitems)):
                        cari = list(filter(lambda x : x.specid == valueitems[vi]['specid'], cars))[0]
                        cari.level = valueitems[vi]['value']

                if paramitems[pi]['id'] == 1149:
                    valueitems = paramitems[pi]['valueitems']
                    for vi in range(len(valueitems)):
                        cari = list(filter(lambda x : x.specid == valueitems[vi]['specid'], cars))[0]
                        cari.energy_type = valueitems[vi]['value']

                if paramitems[pi]['name'].startswith('上市'):
                    valueitems = paramitems[pi]['valueitems']
                    for vi in range(len(valueitems)):
                        cari = list(filter(lambda x : x.specid == valueitems[vi]['specid'], cars))[0]
                        cari.listed_date = valueitems[vi]['value']

                if paramitems[pi]['id'] == 1291:
                    valueitems = paramitems[pi]['valueitems']
                    for vi in range(len(valueitems)):
                        cari = list(filter(lambda x : x.specid == valueitems[vi]['specid'], cars))[0]
                        cari.dist = valueitems[vi]['value']

                if paramitems[pi]['id'] == 1292:
                    valueitems = paramitems[pi]['valueitems']
                    for vi in range(len(valueitems)):
                        cari = list(filter(lambda x : x.specid == valueitems[vi]['specid'], cars))[0]
                        cari.fast_charge = valueitems[vi]['value']

                if paramitems[pi]['id'] == 0 and paramitems[pi]['name'].endswith('(小时)') and len(paramitems[pi]['name']) < 100  :
                    valueitems = paramitems[pi]['valueitems']
                    for vi in range(len(valueitems)):
                        cari = list(filter(lambda x : x.specid == valueitems[vi]['specid'], cars))[0]
                        cari.charge_time = valueitems[vi]['value']

                if paramitems[pi]['id'] == 0 and paramitems[pi]['name'].endswith('百分比'):
                    valueitems = paramitems[pi]['valueitems']
                    for vi in range(len(valueitems)):
                        cari = list(filter(lambda x : x.specid == valueitems[vi]['specid'], cars))[0]
                        cari.fast_charge_percentage = valueitems[vi]['value']

                if paramitems[pi]['id'] == 1185:
                    valueitems = paramitems[pi]['valueitems']
                    for vi in range(len(valueitems)):
                        cari = list(filter(lambda x : x.specid == valueitems[vi]['specid'], cars))[0]
                        cari.maximum_power = valueitems[vi]['value']

                if paramitems[pi]['id'] == 1186:
                    valueitems = paramitems[pi]['valueitems']
                    for vi in range(len(valueitems)):
                        cari = list(filter(lambda x : x.specid == valueitems[vi]['specid'], cars))[0]
                        cari.maximum_torque = valueitems[vi]['value']

                if paramitems[pi]['name'] == '电动机(Ps)':
                    valueitems = paramitems[pi]['valueitems']
                    for vi in range(len(valueitems)):
                        cari = list(filter(lambda x : x.specid == valueitems[vi]['specid'], cars))[0]
                        cari.motor_horsepower = valueitems[vi]['value']

                if paramitems[pi]['id'] == 1148:
                    valueitems = paramitems[pi]['valueitems']
                    for vi in range(len(valueitems)):
                        cari = list(filter(lambda x : x.specid == valueitems[vi]['specid'], cars))[0]
                        cari.volume = valueitems[vi]['value']

                if paramitems[pi]['id'] == 1147:
                    valueitems = paramitems[pi]['valueitems']
                    for vi in range(len(valueitems)):
                        cari = list(filter(lambda x : x.specid == valueitems[vi]['specid'], cars))[0]
                        if len(cari.structure) == 0:
                            cari.structure = valueitems[vi]['value']

                if paramitems[pi]['id'] == 1246:
                    valueitems = paramitems[pi]['valueitems']
                    for vi in range(len(valueitems)):
                        cari = list(filter(lambda x : x.specid == valueitems[vi]['specid'], cars))[0]
                        cari.maximum_speed = valueitems[vi]['value']

                if paramitems[pi]['id'] == 1250:
                    valueitems = paramitems[pi]['valueitems']
                    for vi in range(len(valueitems)):
                        cari = list(filter(lambda x : x.specid == valueitems[vi]['specid'], cars))[0]
                        cari.hundred_km_acceleration = valueitems[vi]['value']

                if paramitems[pi]['id'] == 0 and paramitems[pi]['name'].endswith('政策'):
                    valueitems = paramitems[pi]['valueitems']
                    for vi in range(len(valueitems)):
                        cari = list(filter(lambda x : x.specid == valueitems[vi]['specid'], cars))[0]
                        cari.policy = valueitems[vi]['value']


    return cars


def log(msg):
    print('[LOG] ' + ', ' + time.strftime('%H:%M:%S', time.localtime(time.time())) + ': ' + str(msg))


def getOption():
    pass


if __name__ == "__main__":
    cars = getConfig()
    for car in cars:
        log(car.name + car.structure + car.policy)





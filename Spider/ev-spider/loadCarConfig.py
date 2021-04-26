import json
import time
from Car import CarInfo
from Car import Param
from paramTool import ParamTool
import Serializer


def getConfig():
    paramtool = ParamTool()
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
            paramTypeName = paramtypeitems[pti]["name"]

            if paramTypeName == "基本参数":
                baseParamItems = paramtypeitems[pti]["paramitems"]
                for pi in range(len(baseParamItems)):
                    paramName = paramtool.getParaName(0, pi)
                    valueitems = baseParamItems[pi]['valueitems']
                    for vi in range(len(valueitems)):
                        cari = [x for x in cars if x.specid == valueitems[vi]['specid']][0]
                        #list(filter(lambda x : x.specid == valueitems[vi]['specid'], cars))[0]
                        log(paramName + str(valueitems[vi]['specid']))
                        cari.basic_parameters.append(Param(paramTypeName, paramName, valueitems[vi]['value']))

    return cars


def log(msg):
    print('[LOG] ' + ', ' + time.strftime('%H:%M:%S', time.localtime(time.time())) + ': ' + str(msg))


def getOption():
    pass


if __name__ == "__main__":
    cars = getConfig()
    log(len(cars))
    params = cars[1].basic_parameters
    log(len(params))
    #for p in params:
    #   log(str(cars[1].specid) + "@@@" + p.format())







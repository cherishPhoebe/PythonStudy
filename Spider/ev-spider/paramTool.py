

class ParamTool(object):

    baseParamDic = {
        0:'车型',
        1:'厂商指导价',
        2:'厂商',
        3:'级别',
        4:'能源类型',
        5:'上市日期',
        6:'工信部纯电续航里程(km)',
        7:'快充时间(小时)',
        8:'慢充时间(小时)',
        9:'快充电量百分比',
        10:'最大功率(kw)',
        11:'最大扭矩(N-m)',
        12:'电动机(Ps)',
        13:'长*宽*高(mm)',
        14:'车身结构',
        15:'最高车速(km/h)',
        16:'官方0-100km/h加速(s)',
        17:'实测0-100km/h加速(s)',
        18:'实测100-0km/h制动(s)',
        19:'实测续航里程(km)',
        20:'实测快充时间(小时)',
        21:'实测慢充时间(小时)',
        22:'整车质保'
    }
    
    def getParaName(self, paramType, paramIndex):
        if paramType == 0:
            return self.baseParamDic[paramIndex]

        return ''
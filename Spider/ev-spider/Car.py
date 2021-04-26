
class CarInfo(object):
    """
    车辆信息：
        型号，链接，用户评分，图片，级别，续航里程，发动机，充电时间，官方指导价，折扣后价格，颜色列表
    """
    seriesid = ''
    specid = ''
    name = ''
    url = ''
    score = ''
    image = ''
    level = ''
    energy_type = ''
    listed_date = ''
    dist = ''
    motor = ''
    # 快充时间
    fast_charge = ''
    # 充电时间
    charge_time = ''
    # 快充百分比
    fast_charge_percentage = ''
    # 最大功率
    maximum_power = ''
    # 最大扭矩
    maximum_torque = ''
    # 电动机马力
    motor_horsepower = ''
    # 体积
    volume = ''
    # 结构
    structure = ''
    # 最高车速
    maximum_speed = ''
    # 百公里加速
    hundred_km_acceleration = ''
    # 政策
    policy = ''
    official_price = ''
    discounted_price = ''
    colors = []
    basic_parameters = []
    car_body_parameters = []
    electric_motor_parameters = []
    gearbox_parameters = []
    chassis_steering_parameters = []
    wheel_brake_parameters = []


class BrandInfo(object):
    """
    品牌信息：
        名称，链接，车型列表
    """
    name = ''
    url = ''
    cars = []


class Param(object):

    def __init__(self, param_type, name, value):
        self.param_type = param_type
        self.name = name
        self.value = value
        
    def format(self):
        return self.param_type + '###' + self.name + '###' + self.value
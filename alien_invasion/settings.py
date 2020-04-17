
class Settings():
    """ 存储《外星人入侵》 的所有设置的类 """
    def __init__(self):
        """ 初始化游戏的设置 """
        # 屏幕属性设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230) 
        self.ship_speed_factor = 0.5
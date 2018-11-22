# -*- encoding:utf-8 -*-
# Author: Koctr


class Flight(object):
    """使用属性方法查询航班信息"""
    def __init__(self, name):
        self.flight_name = name

    def checking_status(self):
        """检查航班状态"""
        print("Checking flight %s status" % self.flight_name)
        return 1

    @property
    def flight_status(self):
        """航班状态属性方法"""
        status = self.checking_status()
        if status == 0:
            print("Flight got canceled...")
        elif status == 1:
            print("Flight is arrived...")
        elif status == 2:
            print("Flight has departured already...")
        else:
            print("Can't confirm the flight status...please check later.")

flight = Flight("CA9880")
flight.flight_status

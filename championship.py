from driver import Driver
from grand_pri import GP
from culc_time import Time

class Championship():
    def __init__(self) -> None:
        self.driver_list: list[Driver] = []
        self.grand_pri_list: list[GP] = []
        self.culc_resoult = []
    
    def createDriver(self, driver_name):
        if driver_name in self.driver_list:
            return "This driver alredy exist in Driver list"
        driver = Driver(driver_name)
        self.driver_list.append(driver)
        return driver, "Qo'shildi"

    def getDrivers(self):
        return self.driver_list
    
    def getDriver(self, driver_name):
        for driver in self.driver_list:
            if driver.driver == driver_name:
                return driver_name
        return None

# T2
    def defineGrandPrix(self, gp_name):
        if gp_name in self.grand_pri_list:
            return "This Grand Pri name alredy exist"
        grand_pri = GP(gp_name)
        self.grand_pri_list.append(grand_pri)
        return grand_pri, "Qo'shildi"
    
    def getGrandPrix(self, grand_pri_name):
        for gp in self.grand_pri_list:
            if gp.gp == grand_pri_name:
                return gp.gp
            else:
                None
# T3
    def set_time(self, gp_name, driver_name, finish_time:Time):
        if self.getGrandPrix(gp_name) == None:
            return "Grand Pri mavjud emas"
        if self.getDriver(driver_name) == None:
            return "Driver mavjud emas"
        setting_time = [gp_name, driver_name, finish_time]
        self.culc_resoult.append(list(setting_time))
        return self.culc_resoult
    
    def get_GP_Ranking(self):
        for setting_time in self.culc_resoult:
            for i in setting_time:
                print(i)
            # print(setting_time[2])
        return "finish"

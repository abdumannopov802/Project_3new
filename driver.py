

class Driver():
    def __init__(self, name) -> None:
        self._driver_name = name

    @property
    def driver(self):
        return  self._driver_name

    def __str__(self) -> str:
        return self.driver

    def getName(self):
        return self.driver
from Factory.driverFactory import DriverFactory


class SingletonDriver():
    __instance = DriverFactory().get_driver()

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(SingletonDriver, cls).__new__(cls)
        return cls.__instance

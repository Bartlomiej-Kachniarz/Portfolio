from __future__ import annotations

from abc import ABC, abstractmethod


class AbstractCarsFactory(ABC):
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. Products of one family are usually
    able to collaborate among themselves. A family of products may have several
    variants, but the products of one variant are incompatible with products of
    another.
    """

    @abstractmethod
    def create_electric_car(self) -> AbstractElectric:
        pass

    @abstractmethod
    def create_hybrid_car(self) -> AbstractHybrid:
        pass

    @abstractmethod
    def create_petrol_car(self) -> AbstractPetrol:
        pass


class BMWCarsFactory(AbstractCarsFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_electric_car(self) -> AbstractElectric:
        return BMWElectric()

    def create_hybrid_car(self) -> AbstractHybrid:
        return BMWHybrid()

    def create_petrol_car(self) -> AbstractPetrol:
        return BMWPetrol()


class ToyotaCarsFactory(AbstractCarsFactory):
    def create_electric_car(self) -> AbstractElectric:
        return ToyotaElectric()

    def create_hybrid_car(self) -> AbstractHybrid:
        return ToyotaHybrid()

    def create_petrol_car(self) -> AbstractPetrol:
        return ToyotaPetrol()


class FordCarsFactory(AbstractCarsFactory):
    def create_electric_car(self) -> AbstractElectric:
        return FordElectric()

    def create_hybrid_car(self) -> AbstractHybrid:
        return FordHybrid()

    def create_petrol_car(self) -> AbstractPetrol:
        return FordPetrol()


class AbstractElectric(ABC):
    @abstractmethod
    def get_max_range(self):
        pass

    @abstractmethod
    def get_battery_capacity(self):
        pass


class BMWElectric(AbstractElectric):
    def get_max_range(self):
        return "The electric BMW max range is 500 km."

    def get_battery_capacity(self):
        return "The electric BMW battery capacity is 5 Ah."


class ToyotaElectric(AbstractElectric):
    def get_max_range(self):
        return "The electric Toyota max range is 560 km."

    def get_battery_capacity(self):
        return "The electric Toyota battery capacity is 5.5 Ah."


class FordElectric(AbstractElectric):
    def get_max_range(self):
        return "The electric Ford max range is 480 km."

    def get_battery_capacity(self):
        return "The electric Ford battery capacity is 4.5 Ah."


class AbstractHybrid(ABC):
    @abstractmethod
    def get_fuel_consumption(self):
        pass

    @abstractmethod
    def get_hybrid_type(self):
        pass


class BMWHybrid(AbstractHybrid):
    def get_fuel_consumption(self):
        return "The hybrid BMW fuel consumption is 3l/100 km."

    def get_hybrid_type(self):
        return "The hybrid BMW is of plug-in type."


class ToyotaHybrid(AbstractHybrid):
    def get_fuel_consumption(self):
        return "The hybrid Toyota fuel consumption is 2l/100 km."

    def get_hybrid_type(self):
        return "The hybrid Toyota is of self-charging type."


class FordHybrid(AbstractHybrid):
    def get_fuel_consumption(self):
        return "The hybrid Ford fuel consumption is 4l/100 km."

    def get_hybrid_type(self):
        return "The hybrid Ford is of plug-in type."


class AbstractPetrol(ABC):
    @abstractmethod
    def get_engine_power(self):
        pass

    @abstractmethod
    def get_max_speed(self):
        pass


class BMWPetrol(AbstractPetrol):
    def get_engine_power(self):
        return "The petrol BMW engine power is 240hp."

    def get_max_speed(self):
        return "The petrol BMW max speed is 220km/h."


class ToyotaPetrol(AbstractPetrol):
    def get_engine_power(self):
        return "The petrol Toyota engine power is 180hp."

    def get_max_speed(self):
        return "The petrol Toyota max speed is 190km/h."


class FordPetrol(AbstractPetrol):
    def get_engine_power(self):
        return "The petrol Ford engine power is 200hp."

    def get_max_speed(self):
        return "The petrol Ford max speed is 210km/h."


def client_code(factory: AbstractCarsFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    electric_car = factory.create_electric_car()
    hybrid_car = factory.create_hybrid_car()
    petrol_car = factory.create_petrol_car()

    print(f"{electric_car.get_battery_capacity()}")
    print(f"{electric_car.get_max_range()}")
    print(f"{hybrid_car.get_fuel_consumption()}")
    print(f"{hybrid_car.get_hybrid_type()}")
    print(f"{petrol_car.get_engine_power()}")
    print(f"{petrol_car.get_max_speed()}")


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing factory code with first factory type:")
    client_code(BMWCarsFactory())

    print("\n")

    print("Client: Testing the same factory code with second factory type:")
    client_code(ToyotaCarsFactory())

    print("\n")

    print("Client: Testing the same factory code with third factory type:")
    client_code(FordCarsFactory())

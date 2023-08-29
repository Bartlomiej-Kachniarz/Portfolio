from __future__ import annotations

from abc import ABC, abstractmethod

from shipments import AirShipment, RoadShipment, SeaShipment, Shipment


class Delivery(ABC):
    """The creator class declares a factory method which returns an object
    of a product class. The subclasses provide implementations of this method."""

    @abstractmethod
    def create_transport_mean(self):
        """This is the factory_method.
        Here might be some default implementation of the factory method."""

    def plan_delivery(self) -> float:
        """The Creator class (Delivery) is actually not responsible for creating
        the products. Instead it contains some logic relying on the product objects
        that are returned by the factory method. Child classes can override this logic
        and return different type of product."""

        transport_mean = self.create_transport_mean()

        result = f"""Delivery abstract class: Exactly the same code works with {transport_mean}.
                    \n\n{transport_mean.deliver()}\n"""

        return result


class SeaDelivery(Delivery):
    """Concrete class of a Delivery abstract class. This class has a method
    that override the abstract create_transport_mean() method in parent class."""

    def create_transport_mean(self) -> Shipment:
        return SeaShipment()


class AirDelivery(Delivery):
    """Concrete class of a Delivery abstract class. This class has a method
    that override the abstract create_transport_mean() method in parent class."""

    def create_transport_mean(self) -> Shipment:
        return AirShipment()


class RoadDelivery(Delivery):
    """Concrete class of a Delivery abstract class. This class has a method
    that override the abstract create_transport_mean() method in parent class."""

    def create_transport_mean(self) -> Shipment:
        return RoadShipment()


def client(delivery: Delivery) -> None:
    """The client works with an instance of a concrete Shipment.
    As long as the client works through the base interface,
    it can work with any Shipment's subclass."""

    print(" Client: The delivery works with every subclass!\n", f"{delivery.plan_delivery()}")


if __name__ == "__main__":
    print("\nLogistcs app launched with SeaDelivery:")
    client(SeaDelivery())
    print("\nLogistcs app launched with AirDelivery:")
    client(AirDelivery())
    print("\nLogistcs app launched with RoadDelivery:")
    client(RoadDelivery())

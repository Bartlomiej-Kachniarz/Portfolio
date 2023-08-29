from __future__ import annotations

from abc import ABC, abstractmethod


class Shipment(ABC):
    """The Shipment is an interface that declares operations that all concrete child
    classes of Shipments must implement."""

    @abstractmethod
    def deliver(self) -> str:
        pass


class SeaShipment(Shipment):
    """Concrete child class of Shipment implements its specific interface."""

    @classmethod
    def __str__(cls) -> str:
        return f"{cls.__name__}"

    def deliver(self) -> str:
        return "The Sea Shipment has been successfully delivered."


class AirShipment(Shipment):
    """Concrete child class of Shipment implements its specific interface."""

    @classmethod
    def __str__(cls) -> str:
        return f"{cls.__name__}"

    def deliver(self) -> str:
        return "The Air Shipment has been successfully delivered."


class RoadShipment(Shipment):
    """Concrete child class of Shipment implements its specific interface."""

    @classmethod
    def __str__(cls) -> str:
        return f"{cls.__name__}"

    def deliver(self) -> str:
        return "The Road Shipment has been successfully delivered."

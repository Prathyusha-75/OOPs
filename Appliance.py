from abc import ABC, abstractmethod
class Appliance(ABC):
    @abstractmethod
    def turn_on(self,washing_machine):
        pass
class WashingMachine(Appliance):
    def turn_on(self,washing_machine):
        print(f"turned on {washing_machine}")
class Fridge(Appliance):
    def turn_on(self,fridge):
        print(f"turned on {fridge}")
w1=WashingMachine()
f1=Fridge()
w1.turn_on("washingmachine")
f1.turn_on("fridge")

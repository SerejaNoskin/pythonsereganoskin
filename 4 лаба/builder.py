from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):

    @property  # property позволяет превратить метод класса в атрибут класса

    @abstractmethod  # Абстрактным называется объявленный, но не реализованный метод
    def product(self) -> None:
        pass

    @abstractmethod  # Абстрактным называется объявленный, но не реализованный метод
    def potato(self) -> None:  
        pass

    @abstractmethod
    def pomidor(self) -> None: 
        pass

    @abstractmethod
    def capusta(self) -> None:  #Buider- сложные обьекты создаются по частям
        pass
#обьявление абстрактнызх классов описываме шо они естмь

class Product_Builder(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Shop()

    @property  # property позволяет превратить метод класса в атрибут класса
    def product(self) -> Shop:
        product = self._product
        self.reset()
        return product

    def potato(self) -> None:
        self._product.add("картофель")

    def pomidor(self) -> None:
        self._product.add("помидор")

    def capusta(self) -> None:
        self._product.add("капуста")

#создание асбтрактных классов
class Shop():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"В магазине продаются: {', '.join(self.parts)}", end="")

#вывод продуктов
class Director:

    def __init__(self) -> None:
        self._builder = None

    @property  # property позволяет превратить метод класса в атрибут класса
    def builder(self) -> Builder:
        return self._builder

    @builder.setter  # применяется сеттер к методу builder, то есть делаем метод доступным для записи
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def Magnit(self) -> None:
        self.builder.pomidor()
        self.builder.capusta()

    def ATAK(self) -> None:
        self.builder.potato()
        self.builder.capusta()
#записываемп в  магазин 

if __name__ == "__main__":
    director = Director()
    builder = Product_Builder()
    director.builder = builder

    print("Magnit: ")
    director.Magnit()
    builder.product.list_parts()

    print("\n\nATAK: ")
    director.ATAK()
    builder.product.list_parts()


